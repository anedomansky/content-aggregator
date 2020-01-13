from flask import Flask, request
from backend.services.database_service import DatabaseService
from backend.services.news_website_service import NewsWebsiteService
from backend.services.gaming_website_service import GamingWebsiteService

APP = Flask(__name__)

DATABASE_SERVICE = DatabaseService()
NEWS_WEBSITE_SERVICE = NewsWebsiteService(DATABASE_SERVICE)
GAMING_WEBSITE_SERVICE = GamingWebsiteService(DATABASE_SERVICE)

@APP.route('/')
def initialize_database():
    """
        Creates all necessary tables in the database.
    """
    DATABASE_SERVICE.initialize()
    return {
        "success": "All necessary tables were created successfully!"
    }

@APP.route('/news/all')
def get_all_news_stories():
    """
        Returns all stories that are currently in the news table of the database. 
    """
    stories = NEWS_WEBSITE_SERVICE.get_all_stories()
    return {
        "stories": stories
    }

@APP.route('/news/update')
def update_news_stories():
    """
        Fetches new stories from the specified website of the news category.
        Then parses the HTML and finally adds the new stories to the table in the database.
    """
    website = request.args.get('website')
    NEWS_WEBSITE_SERVICE.update_stories(website)
    return {
        "success": "Updated the news table with the most recent stories from %s." % (website)
    }

@APP.route('/gaming/all')
def get_all_gaming_stories():
    """
        Returns all stories that are currently in the gaming table of the database. 
    """
    stories = GAMING_WEBSITE_SERVICE.get_all_stories()
    return {
        "stories": stories
    }

@APP.route('/gaming/update')
def update_gaming_stories():
    """
        Fetches new stories from the specified website of the gaming category.
        Then parses the HTML and finally adds the new stories to the table in the database.
    """
    website = request.args.get('website')
    GAMING_WEBSITE_SERVICE.update_stories(website)
    return {
        "success": "Updated the news table with the most recent stories from %s." % (website)
    }
