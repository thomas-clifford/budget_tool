# project/test.py

import unittest
from main.users import *

class TestUser(unittest.TestCase):

    test_db = 'src/databases/test.db'
    conn = sqlite3.connect(test_db) # Connect to user database
    cursor = conn.cursor()
    
    test_username = "user"
    test_password = "changeit"

    def setUp(self):
        create_user_db(self.cursor)
        
    def test_create_new_user(self):
        create_user(self.cursor, self.test_username, self.test_password)
    
    def test_create_existing_user(self):
        create_user(self.cursor, self.test_username, self.test_password)
        create_user(self.cursor, self.test_username, self.test_password)

    def test_login_existing_user(self):
        create_user(self.cursor, self.test_username, self.test_password)
        login(self.cursor, self.test_username, self.test_password)
    
    def test_login_non_existing_user(self):
        login(self.cursor, self.test_username, self.test_password)
    
    def test_get_user_id_existing_user(self):
        create_user(self.cursor, self.test_username, self.test_password)
        get_user_id(self.cursor, self.test_username)
    
    def test_get_user_id_non_existing_user(self):
        get_user_id(self.cursor, self.test_username)
    
    def test_user_exists(self):
        create_user(self.cursor, self.test_username, self.test_password)
    

if __name__ == '__main__':
    unittest.main()