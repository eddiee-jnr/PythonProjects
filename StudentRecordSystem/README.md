# 🎓 Student Record Management System

A Python-based command-line interface (CLI) application designed to efficiently manage student data. This project is built as a practical application of core data structures, specifically focusing on the performance benefits of **Dictionary Hashing** for time complexity lookups.

## Features

* **Add Students:** Register new students with a unique ID, Name, Program, and GPA.
* **View Records:** Display a formatted list of all currently enrolled students.
* **Edit Records:** Update a student's Name, Program, or GPA without altering their unique ID key.
* **Delete Records:** Safely remove a student from the database using their ID.
* **GPA Sorting (Manual Bubble Sort):** Automatically migrates dictionary data into a list and runs a custom-built Bubble Sort algorithm to rank students from highest to lowest GPA.
* **Data Persistence:** Fully integrated with Python's `json` module. The database automatically saves all changes to a local `students.json` file and loads them upon startup, preventing any data loss between sessions.

## 🚀 How to Run the App

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/eddiee-jnr/PythonProjects.git](https://github.com/eddiee-jnr/PythonProjects.git)
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd StudentRecordSystem
    ```
3.  **Run the script:**
    ```bash
    python app.py
    ```
