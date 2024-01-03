class Flower:

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        return f"{self.name} is{' ' if self.is_happy else ' not '}happy"
    
    
# Test Cases

rose = Flower("Rose",23)

rose.water(15)
print(rose.status())  

rose.water(34)
print(rose.status())  
  