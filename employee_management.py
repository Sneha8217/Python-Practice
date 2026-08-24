employees = []


def add_employee():
    print("\n===== ADD EMPLOYEE =====")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("Employee added successfully!")


def display_employees():
    print("\n===== EMPLOYEE DETAILS =====")

    if len(employees) == 0:
        print("No employees found.")
        return

    for employee in employees:
        print("----------------------------")
        print("Employee ID:", employee["id"])
        print("Name:", employee["name"])
        print("Department:", employee["department"])
        print("Salary:", employee["salary"])


def search_employee():
    print("\n===== SEARCH EMPLOYEE =====")

    emp_id = input("Enter Employee ID: ")

    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee Found!")
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            return

    print("Employee not found.")


def calculate_average_salary():
    if len(employees) == 0:
        print("No employees available.")
        return

    total_salary = 0

    for employee in employees:
        total_salary += employee["salary"]

    average = total_salary / len(employees)

    print("\n===== SALARY ANALYSIS =====")
    print("Total Employees:", len(employees))
    print("Total Salary:", total_salary)
    print("Average Salary:", round(average, 2))


while True:

    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Calculate Average Salary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        calculate_average_salary()

    elif choice == "5":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Invalid choice. Please try again.")