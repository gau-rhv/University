def cube_sum(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 3
        n //= 10
    return s

def print_armstrong(start, end):
    for num in range(start, end + 1):
        if num == cube_sum(num):
            print(num)

s = int(input("Enter start of range: "))
e = int(input("Enter end of range: "))

print("Armstrong numbers in range:")
print_armstrong(s, e)