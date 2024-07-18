# dog.py

class dog:
    # attribute (variable)
    species = "Canis familiaris"

    # constructor (dunder methods begin and end in __) -> feed in details about object
    # pass self to function so python can modify attributes of itself
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods
    #def description(self):
    #    return(f"{self.name} is {self.age} years old")
    # DUNDER method is an alternative to description, allows you to print(dog) and get a string result without calling print(dog.description())
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def bark(self):
        print(f"{self.name} says bark!")

# boilerplate protects from using script we don't intend to 
# good practice for when importing to other files
if __name__ == "__main__":
    miles = dog("Miles", 4)
    buddy = dog("Buddy", 9)

    print(miles.age)
    print(buddy.age)
    
    #print(miles.description())
    print(miles)
    miles.bark()

    #print(buddy.description())
    print(buddy)
    buddy.bark()