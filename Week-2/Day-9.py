# Mini Project — To-Do App
# n CLI to-do list: add, list, mark complete, delete
# n Save to JSON, persist between runs
# n Load on startup
# n Optional: due dates
# n Push to GitHub
# n First app with persistent data. Real-world pattern.

import json
import os
import time
import datetime    

def load_todo_history(filename='todo_history.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []   
    
def save_todo_history(history, filename='todo_history.json'):
    with open(filename, 'w') as f:
        json.dump(history, f, indent=4)

def add_todo_item(history, item, Datewhen, Due_time):
    entry = {
        "Task": item,
        "Task_id": len(history) + 1,
        "Due_date": Datewhen,
        "status": "pending",
        "Due_time": Due_time,
        "Created_at" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M") 
    }
    history.append(entry)
    print(f"Added: {item} Task ID: {entry['Task_id']} (Due: {Datewhen} at {Due_time})")
    #print(history)
    save_todo_history(history)

def list_tasks(history):
    if not history:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    for entry in history:
        print(f"ID: {entry['Task_id']} | Task: {entry['Task']} | Due: {entry['Due_date']} at {entry['Due_time']} | Status: {entry['status']}")

def mark_task_complete(history, task_id):
    for entry in history:
        if entry['Task_id'] == task_id:
            entry['status'] = 'completed'
            print(f"Marked Task ID {task_id} as completed.")
            save_todo_history(history)
            return
    print(f"Task ID {task_id} not found.")

def delete_task(history):
    try:
        task_id = int(input("Enter task ID to delete: "))
        if task_id < 1 or task_id > len(history):
            print(f"Invalid ID. Only {len(history)} tasks exist.")
            return  # ← inside the if
    except ValueError:
        print("Please enter a valid number.")
        return
    
    for i, entry in enumerate(history):
        if entry['Task_id'] == task_id:
            del history[i]
            print(f"Deleted Task ID {task_id}.")
            save_todo_history(history)
            return
    print(f"Task ID {task_id} not found.")

def check_overdue_tasks(history):
    now = datetime.datetime.now()
    for entry in history:
        if entry['status'] == 'pending':
            if entry['Due_time'] is not None:
                # combine date + time into one datetime object
                due_datetime = datetime.datetime.strptime(entry['Due_date'] + ' ' + entry['Due_time'], "%Y-%m-%d %H:%M")
            else:
                # date only
                due_datetime = datetime.datetime.strptime(entry['Due_date'], "%Y-%m-%d")

            # now ONE comparison
            if due_datetime < now:
                entry['status'] = 'overdue'  # ← don't forget this!
                print(f"Overdue: Task ID {entry['Task_id']} - {entry['Task']} (Due: {entry['Due_date']} at {entry['Due_time']})")
    save_todo_history(history)

# Example usage
if __name__ == "__main__":
    history = load_todo_history()
    check_overdue_tasks(history)
    
    while True:
        print("\n======= TO-DO APP =======")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark task complete")
        print("4. Delete a task")
        print("5. Exit")
        print("=========================")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            # ask user for input, then call add_todo_item()
            title = input("Enter task title: ")
            # what else do you need to ask the user?
            date = input("Enter due date (YYYY-MM-DD): ")
            due_time = input("Enter due time (HH:MM) or press Enter to skip: ")
            due_time = due_time if due_time else None  # ← handles optional time!
            add_todo_item(history, title, date, due_time)  # ← replace with user input
        elif choice == "2":
            list_tasks(history)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark complete: "))
            mark_task_complete(history, task_id)
        elif choice == "4":
            delete_id = int(input("Enter task ID to delete: "))
            delete_task(history, delete_id)
        elif choice == "5":
            break