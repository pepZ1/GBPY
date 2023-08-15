class Cat:
    def __init__(self, name):
        self.name = name
        self.type = "Cat"

    def make_sound(self):
        return "Meow!"


class Dog:
    def __init__(self, name):
        self.name = name
        self.type = "Dog"

    def make_sound(self):
        return "Woof!"


class Bird:
    def __init__(self, name):
        self.name = name
        self.type = "Bird"

    def make_sound(self):
        return "Chirp!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "Cat":
            return Cat(name)
        elif animal_type == "Dog":
            return Dog(name)
        elif animal_type == "Bird":
            return Bird(name)
        else:
            raise ValueError("Unknown animal type")





if __name__ == "__main__":
    factory = AnimalFactory()

animal1 = AnimalFactory.create_animal("Cat", "Whiskers")
animal2 = AnimalFactory.create_animal("Dog", "Buddy")
animal3 = AnimalFactory.create_animal("Bird", "Sunny")

print(animal1.name, animal1.make_sound())  # Вывод: Whiskers Meow!
print(animal2.name, animal2.make_sound())  # Вывод: Buddy Woof!
print(animal3.name, animal3.make_sound())  # Вывод: Sunny Chirp!