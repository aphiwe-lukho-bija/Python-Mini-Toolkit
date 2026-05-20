import helpers

def show_menu():
    print("\n=== Python Mini Toolkit ===")
    print("1. Grade Calculator")
    print("2. To-Do List")
    print("3. Even/Odd Checker")
    print("4. Daily Motivation")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Pick an option: ")
        
        if choice == "1":
            helpers.grade_calc()
        elif choice == "2":
            helpers.todo_list()
        elif choice == "3":
            helpers.even_odd_checker()
        elif choice == "4":
            helpers.motivation_generator()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()