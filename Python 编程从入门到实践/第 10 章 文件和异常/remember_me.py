import json

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input('What is your name? ')
    filename = "username.json"
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()

    prompt = "The current user name is " + username + "?"
    prompt += "\nIf the username is right, please inpurt 'y'; or input 'n'"

    message = input(prompt)
    if message == 'y':
        print("Welcome back, " + username + "!")
    elif message == 'n':
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!") 
    else:
        print('Please inpurt the right message.')
       
    
greet_user()
