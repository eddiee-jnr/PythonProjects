# Main Student List (Student Database)
students = {}

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

# 2. Function to view all students in the database
def view_students():
    print("\n-- Student Records --")
    if not students:
        print("No students in the database! Add students.")
        return

    for student_id, details in students.items():
        print(f"ID: {student_id}, Name: {details['name']}, Program: {details['program']}, GPA: {details['gpa']}")


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

# 5. Function to delete a student from the database
def delete_student():
    print("\n-- Delete a Student --")
    student_id = input("Enter student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} has been deleted.")
    else:
        print("Student not found. Please check the ID and try again.")

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
    # elif choice == '3':
    #     search_student()
    elif choice == '4':
        edit_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Shutting down system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 - 6.")