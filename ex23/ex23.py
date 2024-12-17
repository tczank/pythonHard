#!/usr/bin/python

fruit = [
        ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
        ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red','Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7840]]
]    

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

# test for list comprehension
print("Fruit Comprehension")
print("Question 1")
print('12'+ ' fruit[0][1]', fruit[0][1])

print("Question 2")
print('AAA' + ' fruit[0][2]', fruit[0][2])

print("Question 3")
print('2' + ' fruit[2][1]', fruit[2][1])

print("Question 4")
print('Oranges' + ' fruit[1][0]', fruit[1][0])

print("Question 5")
print('Grapes' + ' fruit[3][0]', fruit[3][0])

print("Question 6")
print('14' + ' fruit[3][1]', fruit[3][1])

print("Question 7")
print('Apples' + ' fruit[0][0]', fruit[0][0])

print("\nCars Comprehension")
print("Question 1")
print('Big' + ' cars[0][1][1]', cars[0][1][1])

print("Question 2")
print('Red cars[1][1][0]', cars[1][1][0])

print("Question 3")
print('1234 cars[2][1][2]', cars[2][1][2])

print("Question 4")
print('White cars[3][1][0]', cars[3][1][0])

print("Question 5")
print('7890 cars[3][1][2]', cars[3][1][2])

print("Question 6")
print('Black cars[0][1][0]', cars[0][1][0])

print("Question 7")
print('34500 cars[0][1][2]', cars[0][1][2])

print("Question 8")
print('Blue cars[2][1][0]', cars[2][1][0])

print("\nLanguages Challenge")
print("Question 1")
print('Slow languages[0][1][0]', languages[0][1][0])

print("Question 2")
print('Alright languages[1][1][1][0]', languages[1][1][1][0])

print("Question 3")
print('Dangerous languages[3][1][1][1]', languages[3][1][1][1])

print("Question 4")
print('Fast languages[4][1][0]', languages[4][1][0])

print("Question 5")
print('Difficult languages[4][1][1][1]', languages[4][1][1][1])

print("Question 6")
print('Fun languages[2][1][1][0]', languages[2][1][1][0])

print("Question 7")
print('Annoying languages[3][1][1][0]', languages[3][1][1][0])

print("Question 8")
print('Weird languages[2][1][1][1]', languages[2][1][1][1])

print("Question 9")
print('Moderate languages[2][1][0]', languages[2][1][0])

print('\nExtra test')
print('cars[1][1][1]', cars[1][1][1]) # Little
print('cars[1][1][0]', cars[1][1][0]) # Red
print('cars[1][0]', cars[1][0]) # Corvette
print('cars[3][1][1]', cars[3][1][1]) # Baby
print('fruit[3][2]', fruit[3][2]) # UR
print('languages[0][1][1][1]', languages[0][1][1][1]) # Mush
print('fruit[2][1]', fruit[2][1]) # 2
print('languages[3][1][0]', languages[3][1][0]) # Fast

