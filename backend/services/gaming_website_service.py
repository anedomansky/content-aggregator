"""
Execute SQL in order to store or retrieve news posts.
"""
import requests
from bs4 import BeautifulSoup

class GamingWebsiteService:
    """
        Service which handles all database interaction for the gaming category.
    """

    def __init__(self, database_service):
        self.__database_service = database_service

    def get_all_stories(self):
        """
            Returns all stories that are currently in the gaming table of the database.
        """
        vg247 = self.__database_service.execute_queries([
            """
                SELECT DISTINCT ON (SNIPPET) SNIPPET,
                LINK
                FROM GAMING
                WHERE WEBSITE = 'vg247'
                ORDER BY
                SNIPPET DESC,
                CREATED DESC;
            """
        ], True)
        gameinformer = self.__database_service.execute_queries([
            """
                SELECT DISTINCT ON (SNIPPET) SNIPPET,
                LINK
                FROM GAMING
                WHERE WEBSITE = 'gameinformer'
                ORDER BY
                SNIPPET DESC,
                CREATED DESC;
            """
        ], True)
        polygon = self.__database_service.execute_queries([
            """
                SELECT DISTINCT ON (SNIPPET) SNIPPET,
                LINK
                FROM GAMING
                WHERE WEBSITE = 'polygon'
                ORDER BY
                SNIPPET DESC,
                CREATED DESC;
            """
        ], True)
        stories = {
            "vg247": vg247,
            "gameinformer": gameinformer,
            "polygon": polygon
        }
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
                top_titles = all_titles[:20]

                queries = []
                for title in top_titles:
                    title_text = title.a.string.replace("'", " ")
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s', DEFAULT);
                        """ % (website, title_text, title.a.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code, website)
        elif website == "polygon":
            url = "https://www.polygon.com/"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                all_titles = soup.findAll("a", {"data-analytics-link": "article"})
                top_titles = all_titles[:20]

                queries = []
                for title in top_titles:
                    title_text = title.string.replace("'", " ")
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s', DEFAULT);
                        """ % (website, title_text, title.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code, website)
        elif website == "gameinformer":
            url = "https://www.gameinformer.com/news"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                all_titles = soup.findAll("h2", {"class": "page-title"})
                top_titles = all_titles[:20]

                queries = []
                for title in top_titles:
                    title_text = title.text.strip().replace("'", " ")
                    queries.append(
                        """
                            INSERT INTO GAMING (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s%s', DEFAULT);
                        """ % (website, title_text, url, title.a.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code, website)
