# Import the json module to work with JSON files
import json
FILE_NAME = "ExpenseTracker - CLI/expenses.json"

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

    # master expense list
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

# 2. add a function to view expenses nicely and well organised with summary
def view_expenses():
    print("\n--- Here is your current expense data ---\n")
    

    if not my_expenses:
        print("No expenses to show yet!")
        return

    # Set up our empty buckets for the math summary
    total_spent = 0
    category_totals = {}

    for items in my_expenses:
        # 2.1. Print the individual expense
        print(f"Date: {items['date']} | Amount: ${items['price']:.2f} | Category: {items['category']} | Description: {items['description']}")

        # 2.2 Add the price to the grand total
        total_spent += items['price']

        # 2.3. Sort the price into the correct category bucket
        # capitalize it so "food" and "Food" don't create two separate buckets
        cat = items['category'].capitalize()
        if cat in category_totals:
            category_totals[cat] += items['price']
        else:
            category_totals[cat] = items['price']

    # 2.4 Print the summary right below the list
    print("\n-------------------------------")
    print(f" TOTAL EXPENSES: ${total_spent:.2f}")
    print("--- Breakdown by Category ---")
    for cat, amount in category_totals.items():
        print(f"{cat}: ${amount:.2f}")
    print("-------------------------------")

# 6. add to function to delete an expense
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
    del_choice = input("\nEnter the number of the expense you want to delete (or 'q' to cancel): ")
    if del_choice.lower() == 'q':
        print("Deletion cancelled.")
        return

    if del_choice.isdigit():
        del_choice = int(del_choice)

        # Make sure the user's input is a valid number corresponding to an expense
        if 1 <= del_choice <= len(my_expenses):
            deleted_item = my_expenses.pop(del_choice - 1)

            # Save the newly shortened list to the file
            save_expenses(my_expenses)
            print(f"\nSuccess! Deleted '{deleted_item['description']}' from your expenses.")
        else:
            print(f"Invalid number. Please choose a number between 1 and {len(my_expenses)}.")

# This matches the if choice.isdigit() check above
    else:
        print("Invalid input. Please enter a valid number (e.g., 1, 2, 3).")



# 7. add to function to update an expense (optional)
def update_expenses():
    print("\n -- Update an expense --")

    if not my_expenses:
        print("No expense to update. Go to add expenses to add")
        return

    counter = 1
    for expense in my_expenses:
        print(f"{counter}. Date: {expense['date']} | Amount: ${expense['price']:.2f} | Category: {expense['category']} | Description: {expense['description']}")
        counter += 1

    # 7.1 ask user to select an expense to update
    up_choice = input("\nEnter the number oh the expense you want to update (or 'q' to cancel): ")
    if up_choice.lower() == 'q':
        print ("Update Cancelled")
        return

    if up_choice.isdigit():
        up_choice = int(up_choice)

        # Make sure the user's input is a valid number corresponding to an expense
        if 1 <= up_choice <= len(my_expenses):
            index = up_choice - 1

            # 7.1 Grab the specific dictionary you want to edit
            target_expense = my_expenses[index]
            print(f"\nEditing: '{target_expense['description']}'")

            # Ask for the new details (using your exact add_expense logic)
            new_date = input("Enter the date (e.g., YYYY-MM-DD): ")
            new_price = input("Enter the price: ")
        # Validate the price input to ensure it's a number
            while True:
                try:
                    new_price = float(new_price)
                    break
                except ValueError:
                    print("Invalid input for price. Please enter a number (e.g., 10.00)")
                    new_price = input("Enter the price: ")
            new_category = input("Enter the category (e.g., Food, Transport): ")
            new_description = input("Enter a quick description: ")

            # 7.2. Swap the old dictionary values with the new ones
            target_expense["date"] = new_date
            target_expense["price"] = new_price
            target_expense["category"] = new_category
            target_expense["description"] = new_description

            #7.3 Save the updated list into the file
            save_expenses(my_expenses)
            print("Expense Successfully updated!")

        else:
            print(f"Invalid number. Please choose a number between 1 and {len(my_expenses)}.")
    else:
        print("Invalid input. Please enter a valid number (e.g., 1, 2, 3).")



# 3. add a while that acts as a menu to call the functions we have created
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add a New Expense")
    print("2. View Expenses")
    print("3. Delete an Expense")
    print("4. Update an Expense")
    print("5. Exit")

    choice = input("Please enter an option below: ")

# this loop act as the main menu and make sure user can enter one
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        update_expenses()
    elif choice == '5':
        print("Always keep tarck of your expenses. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
