import requests
from bs4 import BeautifulSoup

class NewsWebsiteService:
    """
        Service which handles all database interaction for the news category.
    """

    def __init__(self, database_service):
        self.__database_service = database_service

    def get_all_stories(self):
        """
            Returns all stories that are currently in the news table of the database.
        """
        welt = self.__database_service.execute_queries([
            """
                SELECT SNIPPET, LINK FROM NEWS
                WHERE WEBSITE = 'welt'
                ORDER BY CREATED DESC;
            """
        ], True)
        spiegel = self.__database_service.execute_queries([
            """
                SELECT SNIPPET, LINK FROM NEWS
                WHERE WEBSITE = 'spiegel'
                ORDER BY CREATED DESC;
            """
        ], True)
        focus = self.__database_service.execute_queries([
            """
                SELECT SNIPPET, LINK FROM NEWS
                WHERE WEBSITE = 'focus'
                ORDER BY CREATED DESC;
            """
        ], True)
        stories = {
            "welt": welt,
            "spiegel": spiegel,
            "focus": focus,
        }
        return stories

    def update_stories(self, website):
        """
            Fetches new stories from the specified website of the news category.
            Then parses the HTML and finally adds the new stories to the table in the database.
        """
        if website == "welt":
            url = "https://www.welt.de/newsticker/"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                all_titles = soup.findAll("a", {"class": "o-link o-teaser__link"})
                top_titles = all_titles[:20]

                queries = []
                for title in top_titles:
                    title_text = title.get("title").replace("'", " ")
                    queries.append(
                        """
                            INSERT INTO NEWS (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s%s', DEFAULT);
                        """ % (website, title_text, "https://www.welt.de", title.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code)
        elif website == "spiegel":
            url = "https://www.spiegel.de/schlagzeilen/"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                all_titles = soup.findAll("a", {"class": "text-black block"})
                top_titles = all_titles[:20]

                queries = []
                for title in top_titles:
                    title_text = title.get("title").replace("'", " ")
                    queries.append(
                        """
                            INSERT INTO NEWS (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s', DEFAULT);
                        """ % (website, title_text, title.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code)
        elif website == "focus":
            url = "https://www.focus.de/schlagzeilen/"
            result = requests.get(url)
            if result.status_code == 200:
                raw_content = result.content
                soup = BeautifulSoup(raw_content, "html.parser")
                news = soup.find("div", {"class": "news"})
                all_titles = news.findAll("a")
                top_titles = all_titles[:20]

                queries = []
                for title in top_titles:
                    title_text = title.get("title").replace("'", " ")
                    title_text = title.get("title").replace("Newsticker: ", "")
                    queries.append(
                        """
                            INSERT INTO NEWS (WEBSITE, SNIPPET, LINK, CREATED)
                            VALUES ('%s', '%s', '%s', DEFAULT);
                        """ % (website, title_text, title.get("href"))
                    )
                self.__database_service.execute_queries(queries, False)
            else:
                print("Fetching the HTML failed!", result.status_code)
