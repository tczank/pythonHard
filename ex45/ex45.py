#!/usr/bin/python

class Person(object):

    # this is double underscores around init
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes

    def talk(self, words):
        print(f"I am {self.name} and {words}")

becky = Person("Becky", 39, "green")
becky.talk("I am talking here!")

print(becky.__dict__)
print(becky.__class__)
print(becky.__class__.__dict__)
print(dir(becky))
print(becky.talk)
print(getattr(becky, "talk"))
print(becky.__class__.__dict__['talk'])
