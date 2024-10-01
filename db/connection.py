from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import Config


engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    pool_size=Config.SQLALCHEMY_POOL_SIZE,
    max_overflow=Config.SQLALCHEMY_MAX_OVERFLOW
)


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def get_db_session():
    return Session()


def close_db_session(session):
    session.close()