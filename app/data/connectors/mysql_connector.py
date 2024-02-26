from mysql.connector import Error, pooling

class DatabasePool:
    # Class variable to hold the connection pool
    pool = None

    @classmethod
    def initialize_pool(cls, host_name, user_name, user_password, db_name, pool_size=5):
        """Initializes the connection pool with the given parameters."""
        try:
            cls.pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=pool_size,
                pool_reset_session=True,
                host="localhost",
                user="jai",
                password="jai@2301420045",
                database="ems"
            )
            print("Connection pool is created successfully")
        except Error as e:
            print(f"Error while creating connection pool: {e}")

    @classmethod
    def get_connection(cls):
        """Retrieves a connection from the pool."""
        try:
            connection = cls.pool.get_connection()
            return connection
        except Error as e:
            print(f"Error while getting connection: {e}")

# Example usage
if __name__ == "__main__":
    DatabasePool.initialize_pool("host_name", "user_name", "user_password", "db_name")
    # Getting a connection from the pool
    connection = DatabasePool.get_connection()
    if connection:
        print("Successfully retrieved a connection from the pool")
        # Don't forget to close the connection when done
        connection.close()
