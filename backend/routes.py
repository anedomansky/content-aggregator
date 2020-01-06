from flask import Flask
from backend.services.DatabaseService import DatabaseService

app = Flask(__name__)

@app.route('/')
def test_database():
    databaseService = DatabaseService()
    databaseService.initialize()
    return "Established the connection!"
