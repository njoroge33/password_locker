class User:
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.users_list.append(self)

    @classmethod
    def user_exist(cls, user_name, password):
        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return True

        return False
class Credential:
    credentials_list = []

    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password

    def save_credential(self):
        Credential.credentials_list.append(self)

    @classmethod
    def find_by_account_name(cls, account_name):
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    def delete_credential(self):
        Credential.credentials_list.remove(self)
    