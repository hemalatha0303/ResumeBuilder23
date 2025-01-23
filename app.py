from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)  # No need to redefine it after this

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://RBuserdetails:Root@123@localhost/resume_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Root@123'

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        # Check if the email already exists
        if User.query.filter_by(email=email).first():
            return 'Email already exists. Please use a different email.', 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))  # Redirect to login page after signup
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            return 'Login Successful'
        return 'Invalid email or password. Please try again.', 400
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
