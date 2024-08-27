num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a = num1
b = num2
temp_a = a
temp_b = b

while b != 0:
    temp_b = b
    b = a % b
    a = temp_b

gcd = a
lcm = (num1 * num2) // gcd

print(f"The LCM of {num1} and {num2} is {lcm}.")