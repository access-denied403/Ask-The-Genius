import sqlite3

class Database(object):
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        self.table_name = "Table_Example"
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} \
                            (column_1 INT, column_2 TEXT, column_3 REAL)")
        
    def insert_data(self):
        column_1 = int(input("Enter Int: "))
        column_2 = input("Enter String: ")
        column_3 = float(input("Enter Float: "))
        self.cursor.execute(f"INSERT INTO {self.table_name} \
            (column_1, column_2, column_3) VALUES(?,?,?)",(column_1, column_2, column_3))
        
        self.connection.commit()
        print("Data Saved")
    
    def read_data(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor.fetchall():
            print(row)

if __name__ == "__main__":
    database = Database()
    database.insert_data()
    database.read_data()
    database.cursor.close()
    database.connection.close()
