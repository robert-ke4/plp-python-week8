# toolkit.py - Personal Mini-Toolkit Final Project

def todo_list_tool():
    """Tool 1: Manages a dynamic to-do list (add, view, exit)."""
    tasks = ["Learn Python", "Build final project"]
    
    while True:
        print("\n--- QUICK TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Return to Main Menu")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            print("\nCurrent Tasks:")
            if not tasks:
                print("  (Your list is empty)")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"  {idx}. {task}")
        elif choice == "2":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Success: '{new_task}' added to your list.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option. Please choose between 1 and 3.")

def tip_calculator_tool():
    """Tool 2: Calculates total bill split and tip amount per person."""
    print("\n--- TIP CALCULATOR ---")
    try:
        bill = float(input("Enter total bill amount ($): "))
        tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))
        people = int(input("Enter number of people splitting the bill: "))
        
        if bill < 0 or tip_percent < 0 or people <= 0:
            print("Error: Please enter positive values and at least 1 person.")
            return
            
        tip_amount = bill * (tip_percent / 100)
        total_bill = bill + tip_amount
        per_person = total_bill / people
        
        print(f"\n--- BILL BREAKDOWN ---")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill (incl. tip): ${total_bill:.2f}")
        print(f"Each Person Pays: ${per_person:.2f}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def password_checker_tool():
    """Tool 3: Evaluates password strength based on length, digits, and uppercase letters."""
    print("\n--- PASSWORD STRENGTH CHECKER ---")
    password = input("Enter a password to test: ")
    
    length_ok = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    
    print("\n--- EVALUATION REPORT ---")
    print(f"Length >= 8 characters: {'✓' if length_ok else '✗'}")
    print(f"Contains a number: {'✓' if has_digit else '✗'}")
    print(f"Contains an uppercase letter: {'✓' if has_upper else '✗'}")
    
    if length_ok and has_digit and has_upper:
        print("\nResult: Strong Password! 🎉")
    else:
        print("\nResult: Weak Password. Consider making it longer and adding uppercase letters and numbers.")

def main():
    """Main program loop displaying the toolkit menu."""
    print("======================================")
    print("  WELCOME TO YOUR PERSONAL MINI-TOOLKIT")
    print("======================================")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Quick To-Do List")
        print("2. Tip Calculator")
        print("3. Password Strength Checker")
        print("4. Quit Program")
        
        choice = input("Select a tool (1-4): ").strip()
        
        if choice == "1":
            todo_list_tool()
        elif choice == "2":
            tip_calculator_tool()
        elif choice == "3":
            password_checker_tool()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
            break
        else:
            print("\n⚠️ Invalid choice! Please select a valid option between 1 and 4.")

if __name__ == "__main__":
    main()