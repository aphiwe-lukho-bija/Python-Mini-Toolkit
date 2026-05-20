import random

def grade_calc():
    """Calculates average and gives a grade letter"""
    scores = input("Enter scores separated by spaces: ").split()
    scores = [float(s) for s in scores]
    
    if not scores:
        print("No scores entered.")
        return
    
    avg = sum(scores) / len(scores)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Average: {round(avg, 2)} | Grade: {grade}")

def todo_list():
    """Simple to-do list with add, view, remove"""
    tasks = []
    
    while True:
        print("\n1. Add task 2. View tasks 3. Remove task 4. Back")
        choice = input("Choose: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        elif choice == "3":
            if not tasks:
                print("Nothing to remove.")
                continue
            num = int(input("Task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Removed.")
            else:
                print("Invalid number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def even_odd_checker():
    """Checks if number is even/odd and divisible by 5"""
    num = int(input("Enter a number: "))
    
    # Bonus challenge: modulus + and/or
    if num % 2 == 0 and num % 5 == 0:
        print(f"{num} is even AND divisible by 5")
    elif num % 2 == 0 or num % 5 == 0:
        print(f"{num} is even OR divisible by 5")
    else:
        print(f"{num} is odd and not divisible by 5")

def motivation_generator():
    """Returns a random motivational quote"""
    quotes = [
        "Code a little every day.",
        "Errors are proof you tried.",
        "You’re closer than you think.",
        "Debugging builds character.",
        "Small steps, big progress."
    ]
    print("Motivation:", random.choice(quotes))