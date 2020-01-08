class NewsWebsiteService:
    """
        Service which handles all database interaction for the news category.
    """

    def __init__(self, databaseService):
        self.__databaseService = databaseService
        self.__dieWelt = "insert link to the homepage here"
        self.__focus = "insert link to the homepage here"
        self.__spiegel = "insert link to the homepage here"
    
    def getAllStories(self):
        """
            Returns all stories that are currently in the news table of the database.
        """
        stories = self.__databaseService.executeQueries([
            """
                SELECT WEBSITE, SNIPPET, LINK FROM NEWS ORDER BY CREATED DESC; 
            """
        ], True)
        return stories
    
    def updateStories(self, website, databaseService):
        """
            Fetches new stories from the specified website of the news category.
            Then parses the HTML and finally adds the new stories to the table in the database.
        """
        # fetch the HTML form the homepage
        # switch case in order to determine the correct website
        # parse the HTML and extract the stories
        # add the new stories to the database table
