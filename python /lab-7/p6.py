lst = [int(x) for x in input().split()]

elem = int(input())
lst.append(elem)
print(lst)

elems = [int(x) for x in input().split()]
lst.extend(elems)
print(lst)