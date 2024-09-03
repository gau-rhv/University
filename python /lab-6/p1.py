def count_digits_letters(s):
    d = 0
    l = 0

    for c in s:
        if c.isdigit():
            d += 1
        elif c.isalpha():
            l += 1

    return d, l

s = input("Enter a sentence: ")
d, l = count_digits_letters(s)

print("Number of digits:", d)
print("Number of letters:", l)