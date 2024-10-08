class SpecifiedClass:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def display_namespace(self):
        print(self.__dict__)

name = input("Enter name: ")
age = int(input("Enter age: "))
id = input("Enter ID: ")

obj = SpecifiedClass(name, age, id)
obj.display_namespace()