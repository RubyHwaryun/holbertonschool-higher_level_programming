#!/usr/bin/python3

# Define SwimMixin
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Define FlyMixin
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Define Dragon class inheriting from SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Instantiate an object of the Dragon class
draco = Dragon()

# Demonstrate draco's abilities
draco.swim()
draco.fly()
draco.roar()

