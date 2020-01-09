from flask import Flask, request
from backend.services.DatabaseService import DatabaseService
from backend.services.NewsWebsiteService import NewsWebsiteService
from backend.services.GamingWebsiteService import GamingWebsiteService

app = Flask(__name__)

databaseService = DatabaseService()
newsWebsiteService = NewsWebsiteService(databaseService)
gamingWebsiteService = GamingWebsiteService(databaseService)


@app.route('/')
def initializeDatabase():
    """
        Creates all necessary tables in the database.
    """
    databaseService.initialize()
    return {
        "success": "All necessary tables were created successfully!"
    }

@app.route('/news/all')
def getAllStories():
    """
        Returns all stories that are currently in the news table of the database. 
    """
    stories = newsWebsiteService.getAllStories()
    return {
        "stories": stories
    }

@app.route('/news/update')
def updateNewsStories():
    """
        Fetches new stories from the specified website of the news category.
        Then parses the HTML and finally adds the new stories to the table in the database.
    """
    website = request.args.get('website')
    newsWebsiteService.updateStories(website, databaseService)
    return {
        "success": "Updated the news table with the most recent stories from %s." % (website)
    }

@app.route('/gaming/update')
def updateGamingStories():
    """
        Fetches new stories from the specified website of the gaming category.
        Then parses the HTML and finally adds the new stories to the table in the database.
    """
    website = request.args.get('website')
    gamingWebsiteService.updateStories(website, databaseService)
    return {
        "success": "Updated the news table with the most recent stories from %s." % (website)
    }
