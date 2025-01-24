from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask app
app = Flask(__name__)

# Set the secret key (for session and other functionalities)
app.config['SECRET_KEY'] = os.urandom(24)

# Configure the database URI
# Example for SQLite (you can change this to PostgreSQL or any other DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://username:password@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to prevent overhead

# Initialize the database
db = SQLAlchemy(app)

# Routes, models, etc., go here

# Running the app
if __name__ == "__main__":
    app.run(debug=True)
