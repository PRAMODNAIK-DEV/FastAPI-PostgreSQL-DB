from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://pramodDB_owner:bRiMNXHrz85O@ep-snowy-credit-a57tzyfy.us-east-2.aws.neon.tech/pramodDB?sslmode=require'

engine = create_engine(SQLALCHEMY_DATABASE_URL)     # The function from SQLAlchemy is used to create a database engine. It takes the database URL (SQLALCHEMY_DATABASE_URL) as an argument, which specifies the database connection details.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)     # Created using the sessionmaker function from SQLAlchemy's orm module. It configures the session to be used for database operations. The autocommit and autoflush parameters are set to False to ensure more control over transactions.

Base = declarative_base()       # Defined using declarative_base from SQLAlchemy's ext.declarative module. It serves as the base class for declarative models that will be created later.

# Sets up a context manager using the yield keyword. It creates a database session (db) using SessionLocal and yields it to the caller. After the execution within the context is completed, the finally block ensures that the session is closed.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()