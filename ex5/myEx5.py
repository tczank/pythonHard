#!/usr/bin/python

my_name = 'Thomas de Bruce'
my_age = 34 # not a lie
my_height_cm = 178 # cm
my_weight_kg = 98 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

# converting from imperial to international system
my_height = my_height_cm / 2.54
my_weight = my_weight_kg * 2.20462


print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky; try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
