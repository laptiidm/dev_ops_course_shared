import mysql.connector 

class MysqlAdminShopDB:
    def __init__(self, host="localhost", user="adminshop", password="adminshop", database="shop"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        
    def execute_query(self, query, fetch_results=False):
        self.cursor.execute(query)

        if fetch_results:
            return self.cursor.fetchall()
        else:
            self.connection.commit()
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    
    

        