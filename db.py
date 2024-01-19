import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'sqlite:///./test.db'


Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    title = sqlalchemy.Column(sqlalchemy.String(length=255), index=True)
    text = sqlalchemy.Column(sqlalchemy.Text)
    
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())


engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


