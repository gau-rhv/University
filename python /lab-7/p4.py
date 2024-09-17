lst = [int(x) for x in input().split()]

x = int(input())
lst.append(x)
print(lst)

ext = [int(x) for x in input().split()]
lst.extend(ext)
print(lst)