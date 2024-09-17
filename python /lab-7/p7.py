lst = [int(x) for x in input().split()]

result = 1
for num in lst:
    result *= num

print(result)