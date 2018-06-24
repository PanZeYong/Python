import json

def get_stored_number():
    filename = "number.json"
    
    try:
        with open(filename) as file:
            number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    prompt = "Please input your favorite number: "
    filename = "number.json"

    number = input(prompt)
    with open(filename, 'w') as file:
        json.dump(number, file)
    return number

def show_favorite_number():
    number = get_stored_number()
    if number:
        print("I konw your favorite number. It's " + number)
    else:
        number = get_new_number()
        print("I will show your favorite number to you.")

show_favorite_number()
    