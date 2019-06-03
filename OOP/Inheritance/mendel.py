# Define your classes below:
class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        

child = Child()
print(child.eye_color)
print(child.hair_color)
print(child.hair_type)