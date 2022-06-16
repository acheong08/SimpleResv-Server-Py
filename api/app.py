# Imports
import flask
from werkzeug.utils import secure_filename
import hashlib
from random import randint
import json
import os
import sqlite3

# Flask configurations
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'c40a650584b50cb7d928f44d58dcaffc'

# Utilities
def getMD5(plaintext):
    m = md5()
    m.update(plaintext.encode('utf-8'))
    hash = str(m.hexdigest())
    return hash

# Database handlers
class database:
    def __init__():
        # Database structure
        user_schema = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            hash TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
            userID INTEGER NOT NULL,
            start TEXT NOT NULL,
            end TEXT NOT NULL
        );
        '''
        # Database path
        self.db_path = 'Data/database.db'
        # Create the database if it doesn't exist
        if os.path.isfile(self.db_path):
            pass
        else:
            connection = sqlite3.connect(self.db_path)
            connection.executescript(schema)
            connection.commit()
            connection.close()

    # Getting info about reservations
    def getItems(): # Return items that can be reserved based on query parameters
        pass

    # Making a reservation
    def makeResv(): # Add a reservation to the database. Uses collides to check for validity
        pass
    def collides(): # Check if reservation has conflicts with another
        pass

    # Cancelling a reservation
    def cancelResv(): # Takes reservation ID and checks if already passed
        pass

    # Authentication
    def authenticate(email, hash):
        pass

class web_handler:
    # Web handlers
    @app.route('/api/reserve/make', methods=('POST',))
    def makeResv():
        pass

    @app.route('/api/reserve/cancel', methods=('POST',))
    def cancelResv():
        pass

class web_handler_admin(web_handler):
    # Admin features
    @app.route('/api/admin/view', methods=('GET'))
    def view(): # View all reservations for every item
        pass

    @app.route('/api/admin/actions', methods=('GET', 'POST'))
    def manage(): # Manage users, reservations, and clients
        pass
