lst = list(map(int, input("Enter list of numbers separated by spaces: ").split()))

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
step = int(input("Enter step (optional, default is 1): ") or 1)

print(lst[start:end:step])