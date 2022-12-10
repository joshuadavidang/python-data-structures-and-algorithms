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

print()

poodle = Dog("Poodle", 10)
print(poodle.name)
print(poodle.description())
print(poodle.speak("WOOF"))
