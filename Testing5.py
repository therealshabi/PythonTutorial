import os
import sys
import random


# OOPS Concept

class Animal:
    __name = None  # None same as null
    __height = 0  # '__' signifies a private variable (two underscores)
    __weight = 0
    __sound = 0

    # Constructor
    def __init__(self, name, height, weight, sound):  ## Constructor always have name __init__
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    # Setters
    def set_name(self, name):  # self same as this
        self.__name = name;

    def set_height(self, height):  # self same as this
        self.__height = height;

    def set_weight(self, weight):  # self same as this
        self.__weight = weight;

    def set_sound(self, sound):  # self same as this
        self.__sound = sound;

    # Getters
    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):  ## Here {} are also a way to String Formatting in Python
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name, self.__height, self.__weight,
                                                                     self.__sound)


cat = Animal('Whiskers', 33, 10, "Meow")  ## Object Creation

print(cat.toString())


class Dog(Animal):  ##Inheritance Dog class inheriting from Animal
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):  ##Overriding the Constructor
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)  ##Calling constructor of Super Class

    # Setter for Subclass variables
    def set_owner(self, owner):
        self.__owner = owner

    # Getter for SubClass variables
    def get_owner(self, instance, owner):
        return self.__owner

    def get_type(self):
        print("Dog")

    ##Overriding toString function
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His Owner is {}".format(self.get_name(), self.get_height(),
                                                                                     self.get_weight(),
                                                                                     self.get_sound(),
                                                                                     self.__owner)  ##We have to use getters as name,height etc. are private variables

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


dog = Dog("Black Panther", 10, 20, "Bark", "Shahbaz")
print(dog.toString())


class AnimalTesting:  ##Base Class can hold values of Child Classes but not vice versa
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(dog)

dog.multiple_sounds(4)
dog.multiple_sounds()  ##If not defined it will take as None as defined in the function
