from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db

main = Blueprint('main', __name__)

# User signup route
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("User already exists. Please login.")
            return redirect(url_for('main.signup'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully. Please log in.")
        return redirect(url_for('main.login'))

    return render_template('signup.html')

# User login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("Logged in successfully!")
            return redirect(url_for('main.home'))
        else:
            flash("Invalid credentials. Please try again.")
            return redirect(url_for('main.login'))

    return render_template('login.html')

# Home route
@main.route('/')
def index1():
    return render_template('index1.html')  # Ensure home.html exists in templates
