import json
import os
import random
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'bank_data.json')

class BankSystem:
    def __init__(self):
        self.accounts = self.load_data()

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return {}
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def create_account(self, name, pin, initial_balance=0):
        # Generate a flexible 6-digit account number
        while True:
            acc_num = str(random.randint(100000, 999999))
            if acc_num not in self.accounts:
                break
        
        account = {
            'name': name,
            'pin': pin,
            'balance': float(initial_balance),
            'history': [
                {
                    'type': 'Created',
                    'amount': initial_balance,
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            ]
        }
        self.accounts[acc_num] = account
        self.save_data()
        return acc_num

    def authenticate(self, acc_num, pin):
        if acc_num in self.accounts and self.accounts[acc_num]['pin'] == pin:
            return self.accounts[acc_num]
        return None

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    def deposit(self, acc_num, amount):
        if acc_num not in self.accounts:
            return False, "Account not found"
        
        if amount <= 0:
            return False, "Amount must be positive"

        self.accounts[acc_num]['balance'] += amount
        self.accounts[acc_num]['history'].append({
            'type': 'Deposit',
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_data()
        return True, self.accounts[acc_num]['balance']

    def withdraw(self, acc_num, amount):
        if acc_num not in self.accounts:
            return False, "Account not found"

        if amount <= 0:
            return False, "Amount must be positive"
            
        if self.accounts[acc_num]['balance'] < amount:
            return False, "Insufficient funds"

        self.accounts[acc_num]['balance'] -= amount
        self.accounts[acc_num]['history'].append({
            'type': 'Withdraw',
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_data()
        return True, self.accounts[acc_num]['balance']

# Create a singleton instance
bank = BankSystem()
