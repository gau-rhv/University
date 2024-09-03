s = input("Enter a sentence: ")

d = 0
l = 0

for c in s:
    if c.isdigit():
        d += 1
    elif c.isalpha():
        l += 1

print("Number of digits:", d)
print("Number of letters:", l)