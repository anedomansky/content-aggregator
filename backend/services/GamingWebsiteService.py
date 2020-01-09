import requests
from bs4 import BeautifulSoup

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
        if website == "vg247":
            url = "https://www.vg247.com"
        elif website == "gamerant":
            url = "https://gamerant.com"
        elif website == "gameinformer":
            url = "https://www.gameinformer.com"
        else:
            return None
        
        result = requests.get(url);
        print(result.status_code)
        rawContent = result.content
        soup = BeautifulSoup(rawContent)
        print(soup)

        # <p class="title">
        # <a href="https://www.vg247.com/2020/01/07/xbox-series-x-release-date-specs-games-everything-we-know/">Xbox Series X release date, specs, games – everything we know</a>
        # </p>
        # parse the HTML and extract the stories - find a way to get all <p>s with class "title" - then get the url + text from child (<a>)
        # soup.findAll("p", {"class": "title"}) - test this
        # add the new stories to the database table
