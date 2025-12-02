from flask import Flask
from application.database import db
app = None

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///inventry.db"
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()

from application.controllers import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=10000)

