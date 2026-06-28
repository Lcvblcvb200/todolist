from sqlalchemy.orm import sessionmaker
from app.db.database import db

Session = sessionmaker(bind=db)

def getsession():
    try:
        session = Session()
        yield session
    finally:
        session.close()