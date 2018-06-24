filename = "guest.txt"

username = input("Please input your name: ")

with open(filename, 'w') as file_object:
    file_object.write(username)