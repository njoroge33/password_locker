import unittest
from locker import *


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("njoroge", "lim66")

    def tearDown(self):
        User.users = []

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "njoroge")
        self.assertEqual(self.new_user.password, "liM66")

    def test_create_account(self):
        self.new_user.create_account()

        self.assertEqual(len(User.users), 1)

    def test_save_multiple_accounts(self):
        self.new_user.create_account()

        self.new1_user = User("jim", "7Hh")
        self.new1_user.create_account()

        self.assertEqual(len(User.users), 2)

    def test_account_exists(self):
        self.new_user.create_account()

        self.new2_user = User("john", "hey44")
        self.new2_user.create_account()

        user_exists = User.user_exist("john", "hey44")

        self.assertTrue(user_exists)


class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("twitter", "lim33")

    def tearDown(self):
        Credential.credentials = []

    def test_init(self):
        self.assertEqual(self.new_credential.account_name, "twitter")
        self.assertEqual(self.new_credential.password, "lim33")

    def test_save_credential(self):
        self.new_credential.save_credential()

        self.assertEqual(len(Credential.credentials), 1)

    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()

        self.new1_credential = Credential("facebook", "7fr")
        self.new1_credential.save_credential()

        self.assertEqual(len(Credential.credentials), 2)

    def test_find_by_account_name(self):
        self.new_credential.save_credential()
        self.new2_credential = Credential("instagram", "harf")
        new2_credential.save_credential()

        found_credential = Credential.find_by_account_name("instagram")

        self.assertEqual(found_credential.password, new2_credential.password)

    def test_view_all_credentials(self):

        self.assertEqual(Credential.view_all_credentials(), Credential.credentials)

    def test_delete_credentials(self):
        self.new_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials), 0)


if __name__ == "__main__":
    unittest.main()