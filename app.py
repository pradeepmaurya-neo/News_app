from flask import Flask
from routes import bp
from login import login_bp
import os
from post import post_bp

# from flask_cors import CORS


app = Flask(__name__)
# cors=CORS(app)
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY')


# @app.route('/')
# def home1():
#     return "Lets Go 1"



app.register_blueprint(bp)
app.register_blueprint(login_bp)
app.register_blueprint(post_bp)

if __name__ == "__main__":
    app.run(debug=True)