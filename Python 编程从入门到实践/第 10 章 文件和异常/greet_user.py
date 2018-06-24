import json

filename = 'username.json'

with open(filename) as file:
    username = json.load(file)
    print("Welcome back, " + username + "!")