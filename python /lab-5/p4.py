def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
result = factorial(n)

print("The factorial of", n, "is:", result)