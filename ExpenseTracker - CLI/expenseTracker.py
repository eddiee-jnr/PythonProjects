# Your main list in the global scope
my_expenses = []

# FUNCTION DEFINITIONS:
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
    print("\nSuccess! Expense added.")

# 2. add a function to view expenses nicely and well organised
def view_expenses():
    print("\n--- Here is your current expense data ---")
    for items in my_expenses:
        print(f"Date: {items['date']} | Amount: ${items['price']:.2f} | Category: {items['category']} | Description: {items['description']}")


# 3. add a while that acts as a menu to call the functions we have created
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add a New Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Please enter an option (1, 2, or 3): ")

    # The traffic cop only lets one function run based on the choice!
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
