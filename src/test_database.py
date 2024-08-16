# project/test.py

import unittest
from main.users import *
from main.monthly_summaries import *
from main.category import *
from main.sub_categories import *
from main.transactions import *

class TestDatabase(unittest.TestCase):
    
    test_db = 'src/databases/test.db'
    conn = sqlite3.connect(test_db) # Connect to user database
    cursor = conn.cursor() 
        
    def test_create_user_table(self):
        create_user_db(self.cursor)
        self.assertTrue(self.table_exists("Users"), "The Users table does not exist")
    
    def test_create_monthly_summaries_table(self):
        create_monthly_summary_table(self.cursor)
        self.assertTrue(self.table_exists("MonthlySummaries"), "The MonthlySummaries table does not exist")
    
    def test_create_category_table(self):
        create_category_table(self.cursor)
        self.assertTrue(self.table_exists("Categories"), "The Categories table does not exist")
    
    def test_create_sub_categories_table(self):
        create_sub_category_table(self.cursor)
        self.assertTrue(self.table_exists("SubCategories"), "The SubCategories table does not exist")
    
    def test_create_transactions_table(self):
        create_transactions_table(self.cursor)
        self.assertTrue(self.table_exists("Transactions"), "The Transactions table does not exist")
    
    def table_exists(self, name):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
        return self.cursor.fetchone() is not None
    

if __name__ == '__main__':
    unittest.main()