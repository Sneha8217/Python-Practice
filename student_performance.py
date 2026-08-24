def student_performance(name, marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if all(mark >= 35 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    print("\n===== STUDENT PERFORMANCE =====")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)
    print("Grade:", grade)
    print("Result:", result)


print("===== STUDENT PERFORMANCE ANALYZER =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

student_performance(name, marks)