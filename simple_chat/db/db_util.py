from sqlalchemy import create_engine, text as sql_text

from simple_chat import util


def get_engine():
    db_str = util.get_db_str()
    engine = create_engine(db_str, use_batch_mode=True)
    return engine


def install_db_extensions():
    engine = get_engine()
    with engine.begin() as connection:
        print('Installing uuid-ossp for uuid primary_key generation.')
        connection.execute(sql_text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'))
