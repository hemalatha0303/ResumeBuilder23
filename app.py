from flask import Flask,  render_template 
from flask_mysqldb import MySQL
import os
print(os.path.abspath('templates'))

app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root@123'
app.config['MYSQL_DB'] = 'resume_app'  # Make sure this is your database name

mysql = MySQL(app)

def init_db():
    with app.app_context():  # Ensures MySQL connection is within app context
        cursor = mysql.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        mysql.connection.commit()
        cursor.close()

@app.route('/')  # Add this line to define the route
def index1():
    return render_template('index1.html')  # Renders the index.html file from the templates folder


if __name__ == '__main__':
    init_db()  # Initialize the DB when you run the app
    app.run(debug=True)
