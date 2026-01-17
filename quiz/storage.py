import csv
import os
from datetime import datetime

RESULTS_FILE = os.path.join(os.path.dirname(__file__), 'results.csv')

def init_results_file():
    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Name', 'Roll Number', 'Score', 'Total', 'Percentage'])

def save_result(name, roll, score, total):
    init_results_file()
    percentage = (score / total) * 100
    with open(RESULTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            name,
            roll,
            score,
            total,
            f"{percentage:.2f}%"
        ])

def get_all_results():
    init_results_file()
    results = []
    with open(RESULTS_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append(row)
    return results
