import json
import os
from datetime import datetime

CHAT_FILE = os.path.join(os.path.dirname(__file__), 'messages.json')

# Initialize chat file if not exists
if not os.path.exists(CHAT_FILE):
    with open(CHAT_FILE, 'w') as f:
        json.dump([], f)

def get_messages():
    try:
        with open(CHAT_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def add_message(user, text):
    messages = get_messages()
    
    # Keep only last 50 messages to prevent file from getting too big
    if len(messages) > 50:
        messages = messages[-50:]
        
    new_msg = {
        'user': user,
        'text': text,
        'time': datetime.now().strftime('%H:%M')
    }
    messages.append(new_msg)
    
    with open(CHAT_FILE, 'w') as f:
        json.dump(messages, f)
        
    return new_msg
