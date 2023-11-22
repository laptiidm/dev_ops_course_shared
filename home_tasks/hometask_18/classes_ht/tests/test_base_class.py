import os
import sys
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from modules.base_class import MysqlAdminShopDB

class TestMysqlAdminShopDB(unittest.TestCase):

    def setUp(self):
        self.db = MysqlAdminShopDB()

    def test_connection(self):
        self.assertIsNotNone(self.db.connection)

    def test_execute_query(self):
        query1 = f"CREATE TABLE IF NOT EXISTS test_table (id INT, name VARCHAR(255));"
        self.db.execute_query(query1)
        query2 = f"INSERT INTO test_table (id, name) VALUES (43, 'test');"
        self.db.execute_query(query2)
        query3 = f"SELECT * FROM test_table;"
        self.db.execute_query(query3, True)

    def tearDown(self):
        self.db.close_connection()

if __name__ == '__main__':
    unittest.main()
