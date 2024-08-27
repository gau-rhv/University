number = input("Enter a number: ")
digit = input("Enter a digit: ")

count = 0
for char in number:
    if char in digit:
        count += 2

print(f"The digit {digit} occurs {count//2} times in the number {number}.")