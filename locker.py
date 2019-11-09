class User:
    users = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.users.append(self)

   


class Credential:
    pass
    