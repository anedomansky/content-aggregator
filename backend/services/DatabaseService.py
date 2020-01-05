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
        self.__connection_string = "database=%s user=%s password=%s host=%s port=%s" % (self.__database, self.__user, self.__password, self.__host, self.__port)
    
    def executeQuery(self, query):
        """
            Establishes a database connection and executes a query.
        """
        #con = psycopg2.connect(database="content_aggregator", user="db_user", password="postgres", host="127.0.0.1", port="5432")
        con = psycopg2.connect(self.__connection_string)
        print("Connection established successfully!")
        con.close()
