import os
import sys
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from modules.inheritor_class import MysqlExtendedAdmin

class TestMysqlExtendedAdmin(unittest.TestCase):
    def setUp(self):
        self.db = MysqlExtendedAdmin()

    def test_create_shop(self):
        shop_name = "test_table"
        table_exists_query = f"SHOW TABLES LIKE '{shop_name}'"

        self.db.create_shop(shop_name)
        result = self.db.execute_query(table_exists_query, fetch_results=True)

        if len(result) != 0:
            pass
            self.db.drop_shop(shop_name)
        else:
            self.fail(">> table is not created <<")


    def test_add_item(self):
        shop_name = "test_table"
        test_item = {'id': 1234567, 'name': 'Product 1', 'price': 19.99}
        query = f"SELECT * FROM {shop_name} WHERE id='1234567' AND name='Product 1';"

        self.db.create_shop(shop_name)
        self.db.add_item("test_table", test_item)
        result = self.db.execute_query(query, True)

        self.assertNotEqual(result, [], ">> data is not inserted <<")

        self.db.drop_shop(shop_name)
        

    def test_del_item(self):
        shop_name = "test_table"
        test_item = {'id': 1234567, 'name': 'Product 1', 'price': 19.99}
        query = f"SELECT * FROM {shop_name} WHERE id={test_item['id']};"

        self.db.create_shop(shop_name)
        self.db.add_item("test_table", test_item)
        # question - do I need to check that table is created before adding item to it ???
        # add_item_result = self.db.execute_query(query, True)
        # if len(add_item_result) == 0:
        #     self.fail("could not insert value for testing")

        self.db.del_item(shop_name, test_item['id'])
        del_item_result = self.db.execute_query(query, True)

        self.assertEqual(del_item_result, [], ">> data is not deleted <<")

        self.db.drop_shop(shop_name)


    def test_drop_shop(self):
        shop_name = "test_table"
        table_exists_query = f"SHOW TABLES LIKE '{shop_name}'"

        self.db.create_shop(shop_name)
        # question - do I need to check that table is created before deleting ???
        # create_shop_result = self.db.execute_query(query, True)
        # if len(create_shop_result) == 0:
        #     self.fail("could not create table for testing")
        self.db.drop_shop(shop_name)
        result = self.db.execute_query(table_exists_query, fetch_results=True)

        self.assertEqual(result, [], ">> table is not deleted <<")
   
           
    def tearDown(self):
        self.db.close_connection()

if __name__ == '__main__':
    unittest.main()