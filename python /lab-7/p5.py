lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

lst1.extend(lst2)
print(lst1)

item = int(input())
if item in lst1:
    lst1.remove(item)
    print(lst1)
else:
    print("Item not found.")