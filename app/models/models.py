from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, nullable=False , autoincrement=True, unique=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column("id", Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    title = Column("title", String, nullable=False)
    done = Column("done", Boolean, default=False)
    user_id = Column("user_id", Integer, ForeignKey("users.id"))

    def __init__(self, title, user_id, done=False):
        self.title = title
        self.user_id = user_id
        self.done = done