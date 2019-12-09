class Animal():
    def __init__(self,fur):
        self.fur = fur

    def report(self):
        print("Basic type of Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self,fur):
        Animal.__init__(self,fur)
        print("Dog created!")

    def eat(self):
        print("Dog is eating!")
    





# a = Animal()
# a.eat()
# a.report()

b = Dog('Fuzzy')
print(b.fur)
