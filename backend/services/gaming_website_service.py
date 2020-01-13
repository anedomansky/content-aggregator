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

    def get_all_stories(self):
        """
            Returns all stories that are currently in the gaming table of the database.
        """
        stories = self.__database_service.execute_queries([
            """
                SELECT WEBSITE, SNIPPET, LINK FROM GAMING ORDER BY CREATED DESC;
            """
        ], True)
        return stories

    def update_stories(self, website):
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
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s', DEFAULT);
                        """ % (website, title.a.string, title.a.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code)
        elif website == "gamerant":
            url = "https://gamerant.com"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                all_titles = soup.findAll("a", {"class": "bc-title-link"})
                top_titles = all_titles[:10]

                queries = []
                for title in top_titles:
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s%s', DEFAULT);
                        """ % (website, title.string, url, title.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code)
        elif website == "gameinformer":
            url = "https://www.gameinformer.com/news"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                print(soup.prettify())
                all_titles = soup.findAll("h2", {"class": "page-title"})
                top_titles = all_titles[:10]

                queries = []
                for title in top_titles:
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s%s', DEFAULT);
                        """ % (website, title.text.strip(), url, title.a.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
