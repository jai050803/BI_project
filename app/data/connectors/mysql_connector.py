import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.connection = None
        self.host_name = "localhost"
        self.user_name = "jai"
        self.user_password = "jai@2301420045"
        self.db_name = "ems"

    def connect(self):
        """Establishes a connection to the database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def disconnect(self):
        """Closes the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("The connection is closed")

    def execute_query(self, query):
        """Executes a given SQL query on the database."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query):
        """Executes a read query and returns the fetched data."""
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

# Example usage
if __name__ == "__main__":
    db_conn = DatabaseConnection("host_name", "user_name", "user_password", "db_name")
    db_conn.connect()
    # Example query execution
    # db_conn.execute_query("CREATE TABLE Example (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    db_conn.disconnect()
