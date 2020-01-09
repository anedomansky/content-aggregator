import psycopg2

class DatabaseService:
    """
        Connects to the database, executes queries and creates the tables if necessary.
    """

    def __init__(self):
        self.__database = "content_aggregator"
        self.__user = "db_user"
        self.__password = "postgres"
        self.__host = "127.0.0.1"
        self.__port = "5432"
        self.__connection_string = "dbname=%s user=%s password=%s host=%s port=%s" % (self.__database, self.__user, self.__password, self.__host, self.__port)
    
    def executeQueries(self, queries, isSelect):
        """
            Establishes a database connection and executes a list of queries >= 1.
        """
        connection = psycopg2.connect(self.__connection_string)
        print("Connection established successfully!")
        cursor = connection.cursor()
        for query in queries:
            cursor.execute(query)
        
        if isSelect:
            rows = cursor.fetchall()
            connection.close()
            return rows
        else:
            connection.commit()
            connection.close()

    def initialize(self):
        """
            Creates all necessary tables if they do not exist already.
        """
        self.executeQueries([
            """
                CREATE TABLE IF NOT EXISTS GAMING
                (ID SERIAL PRIMARY KEY NOT NULL,
                WEBSITE VARCHAR(50) NOT NULL,  
                SNIPPET VARCHAR(100) NOT NULL,  
                LINK VARCHAR(50) NOT NULL,
                CREATED DATE DEFAULT CURRENT_DATE);
            """,
            """
                CREATE TABLE IF NOT EXISTS NEWS
                (ID SERIAL PRIMARY KEY NOT NULL,
                WEBSITE VARCHAR(50) NOT NULL,  
                SNIPPET VARCHAR(100) NOT NULL,  
                LINK VARCHAR(50) NOT NULL,
                CREATED DATE DEFAULT CURRENT_DATE);
            """
        ], False)
