import random

class WeatherManager:
    def __init__(self):
        self.cities = {
            "New York": {"temp": 5, "condition": "Snow", "icon": "❄️"},
            "London": {"temp": 12, "condition": "Rain", "icon": "🌧️"},
            "Mumbai": {"temp": 32, "condition": "Sunny", "icon": "☀️"},
            "Tokyo": {"temp": 18, "condition": "Cloudy", "icon": "☁️"},
            "Dubai": {"temp": 38, "condition": "Clear", "icon": "🔥"},
            "Paris": {"temp": 15, "condition": "Windy", "icon": "🌬️"}
        }

    def get_weather(self, city=None):
        if not city or city not in self.cities:
            city = random.choice(list(self.cities.keys()))
            
        data = self.cities[city].copy()
        # Add some random fluctuation to temp
        data['temp'] += random.randint(-2, 2)
        data['humidity'] = random.randint(30, 90)
        data['wind_speed'] = random.randint(5, 25)
        data['city'] = city
        
        return data

    def get_all_cities(self):
        return list(self.cities.keys())

weather_mgr = WeatherManager()
