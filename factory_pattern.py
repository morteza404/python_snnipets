import configparser


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def animal_factory(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)    
    animal_type = config.get("Animal", "animal_type")
    if animal_type == "dog":
        return Dog
    elif animal_type == "cat":
        return Cat
    else:
        return None


animal_class = animal_factory("factory.ini")

animal_instance = animal_class()

print(animal_instance.speak())
