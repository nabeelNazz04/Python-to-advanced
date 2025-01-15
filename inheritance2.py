#MULTIPLE INHERITANCE
# Parent Classes
class Father:
    def gardening(self):
        print("I love gardening")
    def skills(self):
        print("Gardening")

class Mother:
    def cooking(self):
        print("I love cooking")
    def skills(self):
        print("Cooking")

# Child Class inheriting from Father and Mother
class Child(Father, Mother):
    def sports(self):
        print("I love sports")
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

# Create an instance of Child and demonstrate functionality
if __name__ == "__main__":
    c = Child()
    c.gardening()
    c.cooking()
    c.sports()
    c.skills() #there the skills is in 3 classes so it ovverrides