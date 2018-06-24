from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, privilege_list):
        super().__init__(first_name, last_name)
        self.privilege_list = Privileges(privilege_list)


