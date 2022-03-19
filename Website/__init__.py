from flask import Flask

# initializing flask
def create_app():
    app = Flask(__name__)
    # encryption config variable
    #app.config['SECRET_KEY'] = "shh"
    
    # import the views
    from .views import views
    
    # register the blueprints with the flask application
    app.register_blueprint(views, url_prefix='/')
    
    # run and define the database classes - if you import a relative file (.something) you need import things individually
    # from .models import Model1, Model
    
    return app