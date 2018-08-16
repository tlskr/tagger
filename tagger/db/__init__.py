"""
Set up database connetions for tests.


Design follows:
    alextechrants.blogspot.com/2013/08/unit-testing-sqlalchemy-apps.html

"""

from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from tagger.config import config


def credential_string(user=None, password=None, host=None, port=None):
    ''' credential string for create_engine string '''

    dct = {
        "user": user or "",
        "password": ":{0}".format(password) if password else "",
        "host": host or "",
        "port": ":{0}".format(port) if port else "",
    }

    if any([user, password, host, port]):
        fmt = "{user}{password}@{host}{port}"
        fmt = "{user}{password}@{host}{port}"
    else:
        fmt = ""

    return fmt.format(**dct)


def create_engine_string(
        service=None, user=None, password=None,
        host=None, port=None, db_name=None):
    ''' string for SqlAlchemy create_engine '''

    dct = {
        "service": service,
        "host_credentials": credential_string(user, password, host, port),
        "db_name": db_name,
    }
    fmt = "{service}://{host_credentials}/{db_name}"

    return fmt.format(**dct)


def get_engine(
        service=None, user=None, password=None,
        host=None, port=None, db=None,
        pool_size=10, max_overflow=20):
    """ creates db connection string for SqlAlchemy """

    return create_engine(
        string_for_create_engine(
            service=config["TEST_DATABASE"]["ServiceName"],
            db=config["TEST_DATABASE"]["DatabaseName"],
        ),
        pool_size=pool_size,
        max_overflow=max_overflow,
    )
