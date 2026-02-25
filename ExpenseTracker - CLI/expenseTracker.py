# Import the json module to work with JSON files
import json
FILE_NAME = "expenses.json"

# FUNCTION DEFINITIONS:
# 4. Create a function to save expenses to the JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# 5. Create a function to load expenses from the JSON file when the app starts
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []

my_expenses = load_expenses()

# 1. Create a function to add a new expense
def add_expense():
    print("\n--- Add a New Expense ---")

    # 1.1. Ask the user for the details and save their answers in variables
    date = input("Enter the date (e.g., YYYY-MM-DD): ")
    price = input("Enter the price: ")
# Validate the price input to ensure it's a number
    while True:
        try:
            price = float(price)
            break
        except ValueError:
            print("Invalid input for price. Please enter a number (e.g., 10.00)")
            price = input("Enter the price: ")
    category = input("Enter the category (e.g., Food, Transport): ")
    description = input("Enter a quick description: ")

# 1.2. Build your dictionary receipt using the variables we just collected
    new_expense = {
        "date": date,
        "price": float(price),
        "category": category,
        "description": description
    }

# 1.3. Add the new dictionary to your main list
    my_expenses.append(new_expense)
    save_expenses(my_expenses)
    print("\nSuccess! Expense added.")

# 2. add a function to view expenses nicely and well organised
def view_expenses():
    print("\n--- Here is your current expense data ---\n")
    for items in my_expenses:
        print(f"Date: {items['date']} | Amount: ${items['price']:.2f} | Category: {items['category']} | Description: {items['description']}")


# 6. add to function to delete an expense (optional)
def delete_expense():
    print("\n --- Delete an Expense ---")

    if not my_expenses:
        print("No expenses to delete.")
        return

# Add Counter for indexing the expenses
    counter = 1
    for expense in my_expenses:
        print(f"{counter}. Date: {expense['date']} | Amount: ${expense['price']:.2f} | Category: {expense['category']} | Description: {expense['description']}")
        counter += 1

# Ask the user to select an expense to delete by its number
    choice = input("Enter the number of the expense you want to delete (or 'q' to cancel): ")
    if choice.lower() == 'q':
        print("Deletion cancelled.")
        return

    if choice.isdigit():
        choice = int(choice) # Convert the string into a real math integer

        # Make sure the user's input is a valid number corresponding to an expense
        if 1 <= choice <= len(my_expenses):
            deleted_item = my_expenses.pop(choice - 1)

            # Save the newly shortened list to the file
            save_expenses(my_expenses)
            print(f"\nSuccess! Deleted '{deleted_item['description']}' from your expenses.")
        else:
            print(f"Invalid number. Please choose a number between 1 and {len(my_expenses)}.")

# This matches the if choice.isdigit() check above
    else:
        print("Invalid input. Please enter a valid number (e.g., 1, 2, 3).")


# 3. add a while that acts as a menu to call the functions we have created
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add a New Expense")
    print("2. View Expenses")
    print("3. Delete an Expense")
    print("4. Exit")

    choice = input("Please enter an option below: ")

# this loop act as the main menu and make sure user can enter one
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
