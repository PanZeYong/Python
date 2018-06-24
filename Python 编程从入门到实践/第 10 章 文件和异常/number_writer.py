import json

# numbers = [2, 3, 4, 5, 6, 7, 8]
prompt = "Please input your favorite number: "
number = input(prompt)

filename = 'numbers.json'
with open(filename, 'w') as file:
    json.dump(number, file)