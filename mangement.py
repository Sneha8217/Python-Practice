students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def display_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students available.")
        return

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


def search_student():
    print("\n--- Search Student ---")

    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

            found = True
            break

    if not found:
        print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            print("1. Update Age")
            print("2. Update Course")
            print("3. Update Marks")

            choice = input("Enter choice: ")

            if choice == "1":
                student["age"] = int(input("Enter new age: "))
                print("Age updated.")

            elif choice == "2":
                student["course"] = input("Enter new course: ")
                print("Course updated.")

            elif choice == "3":
                student["marks"] = float(input("Enter new marks: "))
                print("Marks updated.")

            else:
                print("Invalid choice.")

            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    while True:

        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


main()