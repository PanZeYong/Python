filenames = ['cat.txt', 'dog.txt']

def show(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print("The " + filename + " is not exist.")
    else:
        print(contents)

for filename in filenames:
    show(filename)