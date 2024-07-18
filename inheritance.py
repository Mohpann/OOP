# child inherits parent class

class Parent:
    hair_color = "brown"
    speaks = ["English"]

class Child(Parent): # inherit Parent class by passing through as parameter to child class
    # In constructor you can EXTEND attributes (add attributes) by using super()
    def __init__(self):
        super().__init__()
        self.speaks.append("Russian") # super() takes us up to the super class and creates a constructor __init__() to append Russian to language list

if __name__ == "__main__":
    parent = Parent()
    # if child is declared here it will change parent.speaks to ["English", "Russian"]

    print(parent.hair_color)
    print(parent.speaks)

    # child class MUST be instantiated after we are done dealing with parent class specific attributes
    child = Child()
    print(child.hair_color)
    print(child.speaks)