# daily_reminder.py

# Prompt user for task input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case (requires Python 3.10+)
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Modify message if time-bound
if time_bound == "yes" and "unknown" not in message:
    message += " that requires immediate attention today!"
elif "unknown" not in message:
    message += ". Consider completing it when you have free time."

# Display the reminder
print("\n" + message)
