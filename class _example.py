class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print("Name - ", self.name)
        print("Age ", self.age)


person1 = Person("Madhushan", 25)
print(person1.age)
person1.displayInfo()

person2 = Person("madhushani", 19)
print(person2.displayInfo())
