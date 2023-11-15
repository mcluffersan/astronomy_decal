class Animal:
    def __init__(self, species, name, age): #self is that were modifying itself
        self.species = species #string
        self.name = name #string
        self.age = age #number (float)

    def eat(self):
        print(self.name, " is eating.")

    def make_noise(self, noise):
        print(self.name, "is making noise:", noise)

    def rename(self, new_name):
        self.name = new_name

class Tardigrade(Animal):
    def __init__(self, species, name, age, habitat):
        super().__init__(species, name, age)
        self.habitat = habitat

    def sit_there(self):
        print(self.name, " is sitting there.")

    def colonize(self):
        print(self.name, " has colonized: ", self.habitat)

    def eat(self):
        print(self.name, " is eating like a tardigrade.")



cat = Animal("Cat", "Prince", 1.5)

print(cat.name)
cat.rename("Princess")
print(cat.name)
cat.make_noise("nyah")

greag = Tardigrade("Tardigrade", "greag", 4000, "Hydrothermic Vents")

greag.eat()