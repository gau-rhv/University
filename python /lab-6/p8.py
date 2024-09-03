s = input("Enter a string: ")
char = input("Enter the character to count: ")
count = 0

for c in s:
    if c == char:
        count += 1

print(f"Number of occurrences of '{char}':", count)