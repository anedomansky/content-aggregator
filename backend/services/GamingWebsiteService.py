import requests
from bs4 import BeautifulSoup


class GamingWebsiteService:
    """
        Service which handles all database interaction for the gaming category.
    """

    def __init__(self, database_service):
        self.__database_service = database_service
        self.__vg247 = "insert link to the homepage here"
        self.__gamerant = "insert link to the homepage here"
        self.__gameinformer = "insert link to the homepage here"

    def getAllStories(self):
        """
            Returns all stories that are currently in the gaming table of the database.
        """
        stories = self.__database_service.executeQueries([
            """
                SELECT WEBSITE, SNIPPET, LINK FROM GAMING ORDER BY CREATED DESC;
            """
        ], True)
        return stories

    def updateStories(self, website, database_service):
        """
            Fetches new stories from the specified website of the gaming category.
            Then parses the HTML and finally adds the new stories to the table in the database.
        """
        if website == "vg247":
            url = "https://www.vg247.com"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                all_titles = soup.findAll("p", {"class": "title"})
                top_titles = all_titles[:10]

                queries = []
                for title in top_titles:
                    # print(title.a.string)
                    # print(title.a.get("href"))
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s', DEFAULT);
                        """ % (website, title.a.string, title.a.get("href"))
                    )
                self.__database_service.executeQueries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code)
        elif website == "gamerant":
            url = "https://gamerant.com"
        elif website == "gameinformer":
            url = "https://www.gameinformer.com"
        else:
            return None

        # <p class="title">
        # <a href="https://www.vg247.com/2020/01/07/xbox-series-x-release-date-specs-games-everything-we-know/">Xbox Series X release date, specs, games – everything we know</a>
        # </p>
        # parse the HTML and extract the stories - find a way to get all <p>s with class "title" - then get the url + text from child (<a>)
        # add the new stories to the database table
