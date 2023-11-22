import os
import sys
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import unittest
from modules.base_class import MysqlAdminShopDB

class TestMysqlAdminShopDB(unittest.TestCase):

    def setUp(self):
        self.db = MysqlAdminShopDB()

    def test_connection(self):
        self.assertIsNotNone(self.db.connection)

    def test_execute_query(self):
        create_table_query = "CREATE TABLE IF NOT EXISTS test_table (id INT, name VARCHAR(255));"
        self.db.execute_query(create_table_query)
        self.assertTrue(self.check_table_exists("test_table"))

        insert_data_query = "INSERT INTO test_table (id, name) VALUES (43, 'test');"
        self.db.execute_query(insert_data_query)
        self.assertTrue(self.check_data_exists("test_table", 43, 'test'))

        select_data_query = "SELECT * FROM test_table;"
        result = self.db.execute_query(select_data_query, fetch_results=True)
        self.assertIsNotNone(result)
        self.assertNotEqual(len(result), 0, "No data selected from the table")

    def tearDown(self):
        self.db.close_connection()

    def check_table_exists(self, table_name):
        query = f"SHOW TABLES LIKE '{table_name}';"
        result = self.db.execute_query(query, fetch_results=True)
        return len(result) > 0

    def check_data_exists(self, table_name, id_value, name_value):
        query = f"SELECT * FROM {table_name} WHERE id={id_value} AND name='{name_value}';"
        result = self.db.execute_query(query, fetch_results=True)
        return len(result) > 0

if __name__ == '__main__':
    unittest.main()
