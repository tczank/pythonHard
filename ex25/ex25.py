#!/usr/bin/python


### pre lesson content

def print_number(x):
    print("NUMBER IS: ", x)

rename_print = print_number
rename_print(100)
print_number(100)

x = 10
y = x
print(x)
print(y)

color = "Red"

corvette = {
    "color": color
}

print("LITTLE", corvette["color"], "CORVETTE")

def run():
    print("VROOM")


corvette = {
        "color": "Red",
        "run" : run
}

print("My", corvette["color"], "can go")
corvette["run"]()
####

### STUDY DRILL


def make_car(color, speed, type):
    car = {"color": color, "speed": speed, "type": type}
    return car


fusca_azul = make_car("azul", 100, "fusca")
fusca_preto = make_car("preto", 90, "fusca")
gol_preto = make_car("preto", 120, "gol")


print(fusca_azul)
print(fusca_preto)
print(gol_preto)

