class NewsWebsiteService:
    """
        Service which handles all database interaction for the news category.
    """

    def __init__(self, database_service):
        self.__database_service = database_service
        self.__die_welt = "insert link to the homepage here"
        self.__focus = "insert link to the homepage here"
        self.__spiegel = "insert link to the homepage here"

    def get_all_stories(self):
        """
            Returns all stories that are currently in the news table of the database.
        """
        stories = self.__database_service.execute_queries([
            """
                SELECT WEBSITE, SNIPPET, LINK FROM NEWS ORDER BY CREATED DESC;
            """
        ], True)
        return stories

    def update_stories(self, website):
        """
            Fetches new stories from the specified website of the news category.
            Then parses the HTML and finally adds the new stories to the table in the database.
        """
        # fetch the HTML form the homepage
        # switch case in order to determine the correct website
        # parse the HTML and extract the stories
        # add the new stories to the database table
