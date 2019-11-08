import unittest
from locker import *


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("njoroge", "lim66")

    def tearDown(self):
        User.users = []

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "njoroge")
        self.assertEqual(self.new_user.password, "lim66")

    def test_create_account(self):
        self.new_user.create_account()

        self.assertEqual(len(users), 1)

#     def test_create_multiple_accounts(self):
#         self.new_user.create_account()

#         self.new1_user = User("jim", "7hh")
#         self.new1_user.create_account()

#         self.assertEqual(len(users), 2)

    

    
        
    
# if __name__ == "__main__":
#     unittest.main()