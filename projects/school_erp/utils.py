import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')
TEACHERS_FILE = os.path.join(DATA_DIR, 'teachers.json')

def init_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(STUDENTS_FILE):
        save_data(STUDENTS_FILE, [])
    if not os.path.exists(TEACHERS_FILE):
        save_data(TEACHERS_FILE, [])

def load_data(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        return json.load(f)

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
