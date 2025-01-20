from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


# The Class inherits from the Base class, which is the declarative base created using declarative_base from SQLAlchemy. This establishes the connection between the model and the database table.
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))