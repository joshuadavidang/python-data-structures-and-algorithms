"""
class -> blueprint for how things should be defined, it doesn't contain data
e.g Dog class shows name and type of breed for defining a dog but doesn't contain the data itself
methods -> functions in a class
instance -> object built from class and contains real data, no longer a blueprint but an actual dog

class - form
instance - filled up form
many instances can be created
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"


milo = Dog("Milo", 5)
print(milo.name)
print(milo.description())
print(milo.speak("Woof"))
