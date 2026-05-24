# JSON
# n import json
# n json.dumps() — dict to JSON string
# n json.loads() — JSON string to dict
# n json.dump() / json.load() for files
# n Save calculator history as JSON
# n Load it back on startup

import json
import os

# import importlib
# Day7 = importlib.import_module("Day-7")



def read_calc_history(filename='calc_history.txt'):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            # print(content)
            return content.splitlines()
    except FileNotFoundError:
        return []

result = read_calc_history()

# for i in result:
#     parts = i.strip().split()
#     print(parts)
history_entries = []
for i in result:
    parts = i.strip().split()
    entry = {
            "operand1": float(parts[0]),
            "operator": parts[1],
            "operand2": float(parts[2]),
            "result": float(parts[4])
        }
    history_entries.append(entry)
# print(history_entries)

with open('calc_history.json', 'w') as f:
    json.dump(history_entries, f, indent=4) 

with open('calc_history.json', 'r') as f:
    loaded_history = json.load(f)
    print(json.dumps(loaded_history, indent=2))


# debugging
# print(os.getcwd()) 
# result = read_calc_history()
# print(type(result))
# print(result)

# def save_history_json(history, filename='history.json'):
#     with open(filename, 'w') as f:
#         json.dump(history, f)

# def load_history_json(filename='history.json'):
#     try:
#         with open(filename, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []   
    
# # Example usage
if __name__ == "__main__":
    print("Loading history...")
#     history = load_history_json()
#     print("Loaded history:", history)
    
#     # Simulate adding a calculation to history
#     history.append("2 + 2 = 4")
    
#     save_history_json(history)
#     print("History saved.")
