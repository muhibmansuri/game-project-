import random
import time
from datetime import datetime

# In a real-world scenario, you would use 'requests' to fetch from CoinGecko or Binance
# For this lab, we will create a high-fidelity simulator that behaves like a real-time feed
# but ensures the project works perfectly offline/locally for demo purposes.

class CryptoManager:
    def __init__(self):
        # Initial prices
        self.prices = {
            'BTC': {'price': 65432.10, 'change': 1.2, 'history': [65000 + random.uniform(-500, 500) for _ in range(20)]},
            'ETH': {'price': 3456.78, 'change': -0.5, 'history': [3400 + random.uniform(-50, 50) for _ in range(20)]},
            'SOL': {'price': 145.20, 'change': 5.7, 'history': [140 + random.uniform(-10, 10) for _ in range(20)]},
            'BNB': {'price': 580.45, 'change': 0.3, 'history': [570 + random.uniform(-5, 5) for _ in range(20)]},
            'ADA': {'price': 0.45, 'change': -2.1, 'history': [0.44 + random.uniform(-0.01, 0.01) for _ in range(20)]}
        }

    def update_prices(self):
        """Simulates price movement like a real market ticker."""
        for coin in self.prices:
            volatility = 0.002 # 0.2% max move per tick
            if coin == 'SOL': volatility = 0.005 # More volatile
            
            change_pct = random.uniform(-volatility, volatility)
            self.prices[coin]['price'] *= (1 + change_pct)
            
            # Update history
            self.prices[coin]['history'].append(self.prices[coin]['price'])
            if len(self.prices[coin]['history']) > 30:
                self.prices[coin]['history'].pop(0)
            
            # Calculate 24h change (simulated)
            first_price = self.prices[coin]['history'][0]
            current_price = self.prices[coin]['price']
            self.prices[coin]['change'] = round(((current_price - first_price) / first_price) * 100, 2)
            
            # Round for display
            self.prices[coin]['display_price'] = f"{self.prices[coin]['price']:,.2f}"

    def get_market_data(self):
        self.update_prices()
        data = []
        for symbol, info in self.prices.items():
            data.append({
                'symbol': symbol,
                'name': self._get_name(symbol),
                'price': info['display_price'],
                'raw_price': info['price'],
                'change': info['change'],
                'history': info['history']
            })
        return data

    def _get_name(self, symbol):
        names = {
            'BTC': 'Bitcoin',
            'ETH': 'Ethereum',
            'SOL': 'Solana',
            'BNB': 'Binance Coin',
            'ADA': 'Cardano'
        }
        return names.get(symbol, symbol)

crypto_mgr = CryptoManager()
