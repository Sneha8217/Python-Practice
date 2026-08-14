def analyze_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    total = sum(numbers)
    average = total / len(numbers)

    print("\n===== NUMBER ANALYSIS =====")
    print("Numbers:", numbers)
    print("Largest Number:", max(numbers))
    print("Smallest Number:", min(numbers))
    print("Sum:", total)
    print("Average:", round(average, 2))
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)


print("===== NUMBER ANALYSIS PROGRAM =====")

numbers = []

for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

analyze_numbers(numbers)