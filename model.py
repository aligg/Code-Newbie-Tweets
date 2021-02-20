from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime


class Tweet(db.Model):
    """tweets taken in to db"""
    __tablename__ = "tweets"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    handle = db.Column(db.String(25), nullable=True)
    time_created = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    text = db.Column(db.String(300), nullable=True)
    retweets = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """prettify output"""

        return "<Item item_id=%s handle=%s>" % (self.item_id, self.handle)



def connect_to_db(app, db_uri):

    """Connect the database to app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app, DB_URI
    connect_to_db(app, DB_URI)
    db.create_all()

    print ("Connected to DB, Woohoo!")

