class Dog():

    # class attributes
    species = 'mammeal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        

sam = Dog('huskie', 'sammy')

print(sam.name)