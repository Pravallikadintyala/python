import time
import json
import os
import sys

DATA_FILE = 'meditation_progress.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def display_menu():
    print("\nMeditation and Mindfulness App")
    print("1. Start a Guided Meditation")
    print("2. Start a Breathing Exercise")
    print("3. Start a Meditation Timer")
    print("4. View Progress")
    print("5. Exit")

def guided_meditation():
    print("\nGuided Meditation Session:")
    print("Close your eyes, take a deep breath, and listen to the following guide...")
    # You can add more text or audio-based guides here
    print("Take a deep breath in... and out...")

def breathing_exercise():
    print("\nBreathing Exercise:")
    for i in range(5):
        print("Breathe in...")
        time.sleep(4)
        print("Breathe out...")
        time.sleep(4)
    print("Well done! You have completed the breathing exercise.")
    sys.exit()  # Exit the program when option 2 is selected

def meditation_timer():
    minutes = int(input("Enter meditation duration in minutes: "))
    seconds = minutes * 60
    print(f"Starting timer for {minutes} minutes.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Meditation session completed!")

def view_progress(data):
    if not data:
        print("\nNo meditation sessions logged yet.")
    else:
        print("\nYour Meditation Progress:")
        for entry in data:
            print(f"Session: {entry['session']}, Duration: {entry['duration']} minutes")

def main():
    data = load_data()
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            guided_meditation()
            data.append({"session": "Guided Meditation", "duration": 5})  # Example duration
        elif choice == '2':
            breathing_exercise()
        elif choice == '3':
            meditation_timer()
            minutes = int(input("Enter the duration you just meditated (in minutes): "))
            data.append({"session": "Meditation Timer", "duration": minutes})
        elif choice == '4':
            view_progress(data)
        elif choice == '5':
            save_data(data)
            print("Exiting Meditation and Mindfulness App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
