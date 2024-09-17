lst = list(map(int, input("Enter list of numbers separated by spaces: ").split()))

m = int(input("Enter incorrect value: "))
c = int(input("Enter correct value: "))

if m in lst:
    i = lst.index(m)
    lst[i] = c
    print(lst)
else:
    print("Value not found.")