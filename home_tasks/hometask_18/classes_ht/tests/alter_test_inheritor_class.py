# import unittest
# from modules.inheritor_class import MysqlExtendedAdmin  

# class TestMysqlExtendedAdmin(unittest.TestCase):

#     def setUp(self):
#         self.db = MysqlExtendedAdmin()
#         self.shop_name = "test_table"

#     def tearDown(self):
#         self.db.drop_shop(self.shop_name)
#         self.db.close_connection()

#     def test_create_shop(self):
#         result = self.db.create_shop(self.shop_name)
#         self.assertTrue(result, ">> table is not created <<")

#     def test_add_item(self):
#         self.test_create_shop()  
#         test_item = {'id': 1234567, 'name': 'Product 1', 'price': 19.99}
#         query = f"SELECT * FROM {self.shop_name} WHERE id='1234567' AND name='Product 1';"
#         self.db.add_item(self.shop_name, test_item)
#         result = self.db.execute_query(query, True)
#         self.assertNotEqual(result, [], ">> data is not inserted <<")

#     def test_del_item(self):
#         # Тут можно снова вызвать self.test_create_shop(), если это необходимо
#         test_item = {'id': 1234567, 'name': 'Product 1', 'price': 19.99}
#         query = f"SELECT * FROM {self.shop_name} WHERE id={test_item['id']};"
#         self.db.add_item(self.shop_name, test_item)
#         self.db.del_item(self.shop_name, test_item['id'])
#         del_item_result = self.db.execute_query(query, True)
#         self.assertEqual(del_item_result, [], ">> data is not deleted <<")

#     def test_drop_shop(self):
#         result = self.db.create_shop(self.shop_name)
#         self.assertTrue(result, ">> table is not created <<")
#         self.db.drop_shop(self.shop_name)
#         result = self.db.execute_query(f"SHOW TABLES LIKE '{self.shop_name}'", fetch_results=True)
#         self.assertEqual(result, [], ">> table is not deleted <<")

# if __name__ == '__main__':
#     unittest.main()
