from modules.base_class import MysqlAdminShopDB

class MysqlExtendedAdmin(MysqlAdminShopDB):
    def __init__(self):
        super().__init__()

    def create_shop(self, shop_name):
        query = f"CREATE TABLE {shop_name} (id INT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2));"
        self.execute_query(query)

    def add_item(self, shop_name, item_data):
        query = f"INSERT INTO {shop_name} (id, name, price) VALUES ({item_data['id']}, '{item_data['name']}', {item_data['price']});"
        self.execute_query(query)

    def del_item(self, shop_name, item_id):
        query = f"DELETE FROM {shop_name} WHERE id = {item_id}"
        self.execute_query(query)

    def drop_shop(self, shop_name):
        query = f"DROP TABLE {shop_name}"
        self.execute_query(query)

