from flask import Blueprint, render_template

# this file is a blueprint of the application, defining how all the files are organized
views = Blueprint('views', __name__)

## defining the views

# the home page function
@views.route('/')
def index():
    # return the home page
    return render_template("index.html")

# the home page function
@views.route('/about')
def home():
    # return the home page
    return render_template("about.html")