
lst = [int(i) for i in input("Enter numbers separated by spaces: ").split()]
x = int(input("Enter a number to append: "))
lst.append(x)
print("List after appending:", lst)
ext = [int(i) for i in input("Enter numbers to extend the list: ").split()]
lst.extend(ext)
print("List after extending:", lst)