#!/usr/bin/python

becky = {
        "name": "Becky",
        "age": 34,
        "eyes": "green"
}

def talk(who, words):
    print(f"I an {who['name']} and {words}")

talk(becky, "I am talking here!")
