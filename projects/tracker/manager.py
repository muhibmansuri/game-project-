import csv
import os
from datetime import datetime

# File to store expenses
FILE_PATH = os.path.join(os.path.dirname(__file__), 'expenses.csv')

def init_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def add_expense(category, amount, description):
    init_file()
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(FILE_PATH, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, float(amount), description])
    return True

def get_expenses():
    init_file()
    expenses = []
    with open(FILE_PATH, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(row)
    # Return reversed to show latest first
    return expenses[::-1]

def get_summary():
    """Returns total spent and breakdown by category for charts"""
    expenses = get_expenses()
    total = 0.0
    by_category = {}

    for e in expenses:
        amt = float(e['Amount'])
        cat = e['Category']
        total += amt
        if cat in by_category:
            by_category[cat] += amt
        else:
            by_category[cat] = amt
    
    return {
        'total': round(total, 2),
        'breakdown': by_category
    }
