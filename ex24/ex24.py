#!/usr/bin/python


# pre lesson content

email = {
    "From": "j.smith@example.com",
    "To": "zed.shaw@example.com",
    "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU!!!"
}

#print(email)

messages = [
    {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
    {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
    {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
    {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'},
]

#print(messages[0]['to'])

#print(messages[0]['from'])

#print(messages[0]['message'])

#print(messages[1]['to'])

#print(messages[1]['from'])

#print(messages[1]['message'])
########################################

fruit = [
{'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
{'kind': 'Oranges', 'count': 1, 'rating': 'B'},
{'kind': 'Pears',
'count': 2, 'rating': 'A'},
{'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
]

cars = [
{'type': 'Cadillac', 'color': 'Black',
'size': 'Big', 'miles': 34500},
{'type': 'Corvette', 'color': 'Red',
'size': 'Little', 'miles': 1000000},
{'type': 'Ford', 'color': 'Blue',
'size': 'Medium', 'miles': 1234},
{'type': 'BMW', 'color': 'White',
'size': 'Baby', 'miles': 7890}
]

languages = [
{'name': 'Python', 'speed': 'Slow',
'opinion': ['Terrible', 'Mush']},
{'name': 'JavaScript', 'speed': 'Moderate',
'opinion': ['Alright', 'Bizarre']},
{'name': 'Perl6', 'speed': 'Moderate',
'opinion': ['Fun', 'Weird']},
{'name': 'C', 'speed': 'Fast',
'opinion': ['Annoying', 'Dangerous']},
{'name': 'Forth', 'speed': 'Fast',
'opinion': ['Fun', 'Difficult']},
]


print("Fruit Comprehension")
print("Question 1")
print('12'+ ' fruit[0]["count"]', fruit[0]['count'])

print("Question 2")
print('AAA' + ' fruit[0]["rating"]', fruit[0]["rating"])

print("Question 3")
print('2' + ' fruit[2]["count"]', fruit[2]["count"])

print("Question 4")
print('Oranges' + ' fruit[1]["kind"]', fruit[1]["kind"])

print("Question 5")
print('Grapes' + ' fruit[3]["kind"]', fruit[3]["kind"])

print("Question 6")
print('14' + ' fruit[3]["count"]', fruit[3]["count"])

print("Question 7")
print('Apples' + ' fruit[0]["kind"]', fruit[0]["kind"])

print("\nCars Comprehension")
print("Question 1")
print('Big' + ' cars[0]["size"]', cars[0]["size"])

print("Question 2")
print('Red cars[1]["color"]', cars[1]["color"])

print("Question 3")
print('1234 cars[2]["miles"]', cars[2]["miles"])

print("Question 4")
print('White cars[3]["color"]', cars[3]["color"])

print("Question 5")
print('7890 cars[3]["miles"]', cars[3]["miles"])

print("Question 6")
print('Black cars[0]["color"]', cars[0]["color"])

print("Question 7")
print('34500 cars[0]["miles"]', cars[0]["miles"])

print("Question 8")
print('Blue cars[2]["color"]', cars[2]["color"])

print("\nLanguages Challenge")
print("Question 1")
print('Slow languages[0]["speed"]', languages[0]["speed"])

print("Question 2")
print('Alright languages[1]["opinion"][0]', languages[1]["opinion"][0])

print("Question 3")
print('Dangerous languages[3]["opinion"][1]', languages[3]["opinion"][1])

print("Question 4")
print('Fast languages[4]["speed"]', languages[4]["speed"])

print("Question 5")
print('Difficult languages[4]["opinion"][1]', languages[4]["opinion"][1])

print("Question 6")
print('Fun languages[2]["opinion"][0]', languages[2]["opinion"][0])

print("Question 7")
print('Annoying languages[3]["opinion"][0]', languages[3]["opinion"][0])

print("Question 8")
print('Weird languages[2]["opinion"][1]', languages[2]["opinion"][1])

print("Question 9")
print('Moderate languages[2]["speed"]', languages[2]["speed"])


