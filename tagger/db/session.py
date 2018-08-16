from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tagger.config import config

from . import create_engine_string


def get_engine(config):
    engine_string = create_engine_string(
        service=config['database']['service'],
        host=config['database']['host'],
        db_name=config['database']['name'],
        user=config['credentials']['user'],
        password=config['credentials']['password'],
    )

    engine = create_engine(engine_string, echo=True)
    return engine


def get_session(config=config):
    engine = get_engine(config)
    Session = sessionmaker(bind=engine)
    return Session
