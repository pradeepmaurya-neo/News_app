from flask import Flask
from routes import bp
from login import login_bp
# from flask_cors import CORS


app = Flask(__name__)
# cors=CORS(app)

# @app.route('/')
# def home1():
#     return "Lets Go 1"



app.register_blueprint(bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(debug=True)