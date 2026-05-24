# WEEKLY MINI-PROJECT - Week 2
# Habit Tracker CLI — track daily habits with streaks. Add habits, mark complete, see your streak count, save to JSON. You'll
# actually use this in real life.
# n Habit dict: {name, created_date, completions: [date strings]}
# n Functions: add_habit, complete_today, show_streaks
# n Calculate streak = consecutive completion days from today backwards
# n Save to habits.json, load on startup
# n BONUS: weekly summary showing % completion per habit

from json_util import load_json, save_json
from datetime import datetime, timedelta
import os

HABITS_FILE = 'habits.json'

def add_habit(habits, name):
    if any(h['name'] == name for h in habits):
        print(f"Habit '{name}' already exists.")
        return
    habit = {
        'name': name,
        'created_date': datetime.now().strftime('%Y-%m-%d'),
        'completions': []
    }
    habits.append(habit)
    print(f"Habit '{name}' added.")

def complete_today(habits, name):
    habit = next((h for h in habits if h['name'] == name), None)
    if not habit:
        print(f"Habit '{name}' not found.")
        return
    today_str = datetime.now().strftime('%Y-%m-%d')
    if today_str in habit['completions']:
        print(f"Habit '{name}' already marked complete for today.")
        return
    habit['completions'].append(today_str)
    print(f"Habit '{name}' marked complete for today.")

def calculate_streak(habit):
    if not habit['completions']:
        return 0
    completions = set(habit['completions'])
    streak = 0
    current_date = datetime.now()
    while current_date.strftime('%Y-%m-%d') in completions:
        streak += 1
        current_date -= timedelta(days=1)
    return streak

def show_streaks(habits):
    if not habits:
        print("No habits to show.")
        return
    for habit in habits:
        streak = calculate_streak(habit)
        print(f"Habit: {habit['name']}, Streak: {streak} days")

def main():
    habits = load_json(HABITS_FILE) if os.path.exists(HABITS_FILE) else []
    while True:
        print("\nHabit Tracker CLI")
        print("1. Add Habit")
        print("2. Complete Today's Habit")
        print("3. Show Streaks")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter habit name: ")
            add_habit(habits, name)
            save_json(habits, HABITS_FILE)
        elif choice == '2':
            name = input("Enter habit name to complete: ")
            complete_today(habits, name)
            save_json(habits, HABITS_FILE)
        elif choice == '3':
            show_streaks(habits)
        elif choice == '4':
            save_json(habits, HABITS_FILE)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")