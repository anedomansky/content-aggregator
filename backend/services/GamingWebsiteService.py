class GamingWebsiteService:
    """
        Service which handles all database interaction for the gaming category.
    """

    def __init__(self, databaseService):
        self.__databaseService = databaseService
        self.__vg247 = "insert link to the homepage here"
        self.__gamerant = "insert link to the homepage here"
        self.__gameinformer = "insert link to the homepage here"
    
    def getAllStories(self):
        """
            Returns all stories that are currently in the gaming table of the database.
        """
        stories = self.__databaseService.executeQueries([
            """
                SELECT WEBSITE, SNIPPET, LINK FROM GAMING ORDER BY CREATED DESC; 
            """
        ], True)
        return stories
    
    def updateStories(self, website, databaseService):
        """
            Fetches new stories from the specified website of the gaming category.
            Then parses the HTML and finally adds the new stories to the table in the database.
        """
        # fetch the HTML form the homepage
        # switch case in order to determine the correct website
        # parse the HTML and extract the stories
        # add the new stories to the database table
