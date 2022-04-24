from cgitb import text
from enum import unique
from .database import Base
from sqlalchemy import TIME, Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False,
                     server_default=text('now()'))


class User(Base):
    __tablename__ = "users"

    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False,
                     server_default=text('now()'))
