from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Tweet(db.Model):
    """tweets taken in to db"""

    __tablename__ = "tweets"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    handle = db.Column(db.String(25), nullable=True)
    time_created = db.Column(db.Datetime, nullable=True)
    text = db.Column(db.String(300), nullable=True)
    retweets = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """prettify output"""

        return "<Item item_id=%s handle=%s>" % (self.item_id, self.handle)
        

def connect_to_db(app, db_uri="postgresql:///newb"):
    """Connect the database to app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB, Woohoo!"
