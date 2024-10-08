class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")        

p = person("Alice")
p2 = person("Bob")
p3 = person("Charlie")

p.introduce()
p2.introduce()
p3.introduce()