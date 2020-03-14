from __future__ import with_statement

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from simple_chat import util

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Custom code
# -------------------------------------------------------------------------------------------
from simple_chat.database import sql_db  # noqa
target_metadata = sql_db.metadata

if config.get_main_option('sqlalchemy.url') is None:
    config.set_main_option('sqlalchemy.url', util.get_db_str())

# Import every model
from simple_chat.db.models import *

ALEMBIC_DEFAULT_OPTIONS = dict(
    target_metadata=target_metadata, compare_type=True, compare_server_default=True
)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, literal_binds=True, **ALEMBIC_DEFAULT_OPTIONS)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, **ALEMBIC_DEFAULT_OPTIONS)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
