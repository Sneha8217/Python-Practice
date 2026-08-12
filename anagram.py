str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")
else:
    frequency = {}

    for char in str1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in str2:
        if char not in frequency:
            print("Not Anagram")
            break

        frequency[char] -= 1

    else:
        if all(value == 0 for value in frequency.values()):
            print("Anagram")
        else:
            print("Not Anagram")