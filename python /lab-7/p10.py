n = int(input("Enter number of items in the list: "))
lst = []

for _ in range(n):
    x = int(input("Enter a number: "))
    lst.append(x)

res = 1
for i in lst:
    res *= i

print(res)