import json

filename = 'numbers.json'
with open(filename) as file:
    number = json.load(file)

print("I know your favorite number! It's " + number)