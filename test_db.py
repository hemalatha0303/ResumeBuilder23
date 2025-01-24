from flask import Flask
from app.db import db  # Import the db object

def test_db_connection():
    try:
        # Try connecting to the database and creating a test table
        with app.app_context():
            db.create_all()  # This will create all the tables, if not already created
            print("Database connection is successful!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

# Set up Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Root%40123@localhost/resume_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Call the test function to check DB connection
test_db_connection()
