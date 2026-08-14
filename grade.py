def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))

    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

total = sum(marks)
percentage = total / 5
grade = calculate_grade(percentage)

print("\n===== RESULT =====")
print("Student Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)