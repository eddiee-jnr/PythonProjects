import json

# add and load data from file
FILE_NAME = "StudentRecordSystem/students.json"

# Main Student List (Student Database)
students = {}

def load_data():
    # Tell Python to modify the master database
    global students
    try:
        # open the file and load the JSON data into our dictionary
        with open(FILE_NAME, 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, just start empty
        students = {}

def save_data():
    # Open the file in 'write' mode and dump the dictionary into it
    with open(FILE_NAME, 'w') as file:
        json.dump(students, file, indent=4)

# 1. Function to add students to the database
def add_students():
    print("\n-- Add a New Student --")

    student_id = input("Enter student ID: ")

    # Checking the student database for existing student
    if student_id in students:
        print("Student ID already exists. Please try again.")
        return

    name = input("Enter student name: ")
    program = input("Enter student program: ")

    # make sure user enters a valid GPA
    while True:
        try:
            gpa = float(input("Enter student GPA: "))
            break
        except ValueError:
            print("Invalid GPA. Please enter a valid number (1.0 to 4.0).")

    # Create a dictionary to hold the student details
    student_details = {
        "name": name,
        "program": program,
        "gpa": gpa
    }

    # Add the new student details to the main database using the ID as the key
    students[student_id] = student_details

    #print the name and ID just added
    print(f"\nSuccess! {name} (ID: {student_id}) has been added.")
    save_data() # Save the added students to the databse file

# 2. Function to view all students in the database and sort from highest to lowest GPA
def view_students():
    print("\n-- Student Records --")
    if not students:
        print("No students in the database! Add students.")
        return

# 2.1 Sort the students by GPA in descending order
    # 2.1 create a list and add the student details to it
    student_list = []

    for student_id, details in students.items():
        # pack everything, including the ID, into a single dictionary
        student_record = {
            "id": student_id,
            "name": details['name'],
            "program": details['program'],
            "gpa": details['gpa']
        }
        student_list.append(student_record)

    # 2.2 perform manual bubble sort(highest to lowest GPA)
    n = len(student_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if student_list[j]['gpa'] < student_list[j+1]['gpa']:
                #swa them if the left GPA is smalller than the right GPA
                student_list[j], student_list[j+1] = student_list[j+1], student_list[j]

    # 2.3 print the sorted list
    for student in student_list:
        print(f"ID: {student['id']}, Name: {student['name']}, Program: {student['program']}, GPA: {student['gpa']}")

# 3. Function to Search for a student by ID
def search_student():
    print("\n-- Search ...")
    student_id = input("Enter student ID to search: ")

    if student_id in students:
        details = students[student_id]
        print(f"ID: {student_id}, Name: {details['name']}, Program: {details['program']}, GPA: {details['gpa']}")
    else:
        print("Student not found. Please check the ID and try again.")

# 4. Function to edit student details except ID
def edit_student():
    print("\n-- Update Student Details --")
    student_id = input("Enter student ID to update: ")

    if student_id in students:
        name = input("Enter new name (leave blank to keep current): ")
        program = input("Enter new program (leave blank to keep current): ")

        while True:
            gpa_input = input("Enter new GPA (leave blank to keep current): ")
            if gpa_input == "":
                gpa = students[student_id]['gpa']  # Keep current GPA
                break
            try:
                gpa = float(gpa_input)
                break
            except ValueError:
                print("Invalid GPA. Please enter a valid number (1.0 to 4.0)")

        # Update the student details with new values provided
        if name:
            students[student_id]['name'] = name
        if program:
            students[student_id]['program'] = program
        students[student_id]['gpa'] = gpa

        print(f"\nSuccess! Student ID {student_id} has been updated.")
    else:
        print("Student not found. Please check the ID and try again.")
    save_data() # Save the updated database after editing

# 5. Function to delete a student from the database
def delete_student():
    print("\n-- Delete a Student --")
    student_id = input("Enter student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} has been deleted.")
    else:
        print("Student not found. Please check the ID and try again.")
    save_data() # Save the updated database after deletion



# Load existing data before starting the menu
load_data()


# --- MAIN MENU ---
while True:
    print("\n=== Student Record Management ===")
    print("1. Add a Student")
    print("2. View Students")
    print("3. Search")
    print("4. Edit Details")
    print("5. Delete")
    print("6. Exit")

    choice = input("Enter an option: ")

    if choice == '1':
        add_students()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        edit_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Shutting down system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 - 6.")