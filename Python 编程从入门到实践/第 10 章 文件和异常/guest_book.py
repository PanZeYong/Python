filename = 'guest_book.txt'

prompt = "\nPlease enter your name:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    name = input(prompt)

    if name != 'quit':
        message = 'Hello ' + name + ", welcome to here!"
        print(message)
        with open(filename, 'a') as file_object:
            file_object.write(message + "\n")
    else:
        break