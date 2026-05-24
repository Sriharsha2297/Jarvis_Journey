import os
import time
import datetime 
import json   

def load_todo_history(filename='todo_history.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []   
    
def save_todo_history(history, filename='todo_history.json'):
    with open(filename, 'w') as f:
        json.dump(history, f, indent=4)