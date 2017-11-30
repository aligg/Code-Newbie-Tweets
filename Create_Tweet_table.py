from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData, Integer
# modify the below postgresql address with you info
db_string = "postgresql://username:password@localhost/newb"
db = create_engine(db_string)
meta = MetaData(db)
tweets_table = Table('tweets', meta,
                        Column('item_id', Integer, autoincrement=True,primary_key=True, nullable=False),
                        Column('handle', String(25), nullable=True),
                        Column('time_created', String),
                        Column('text', String(300), nullable=True),
                        Column('retweets', Integer, nullable=True))

with db.connect() as conn:
   tweets_table.create()


