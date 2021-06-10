from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

 # should be after initialization because app is used in routes

if __name__ == "__main__":
    from routes import *
    app.run(port = 5000, debug = True)
