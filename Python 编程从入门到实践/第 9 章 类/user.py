class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attenpts = 0

    def describe_user(self):
        return self.first_name + " " + self.last_name

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attenpts += 1

    def reset_login_attempts(self):
        self.login_attenpts = 0

# user = User("Julian", "Pan")
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attenpts)
# user.reset_login_attempts()
# print(user.login_attenpts)