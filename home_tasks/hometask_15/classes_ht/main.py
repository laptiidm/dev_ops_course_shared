from base_class import MysqlAdminShopDB
from inheritor_class import MysqlExtendedAdmin

extended_admin = MysqlExtendedAdmin()

extended_admin.create_shop("shop")

item1 = {'id': 1, 'name': 'Product 1', 'price': 19.99}
item2 = {'id': 2, 'name': 'Product 2', 'price': 24.99}
item3 = {'id': 3, 'name': 'Product 3', 'price': 34.99}
extended_admin.add_item("shop", item1)
extended_admin.add_item("shop", item2)
extended_admin.add_item("shop", item3)

item_id_for_delete = 2
extended_admin.del_item("shop", item_id_for_delete)

extended_admin.drop_shop("shop")










