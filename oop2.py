class Circle():

    pi = 3.14159

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return ((self.radius * self.radius) * self.pi)

    def circumfrence(self):
        return 2 * self.pi * self.radius

mycircle = Circle(5)

print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumfrence())