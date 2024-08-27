def calc_ops(a, b):
    s = a + b
    sub = a - b
    mul = a * b
    return s, sub, mul

a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))

s, sub, mul = calc_ops(a, b)

print("Sum:", s)
print("Subtraction:", sub)
print("Multiplication:", mul)