import argparse

from alembic import command  # type: ignore
from alembic.config import Config  # type: ignore

from simple_chat import util
from simple_chat.db import db_util


def parse_args():
    parser = argparse.ArgumentParser(description='Migrate the DB up.')
    parser.add_argument('-c', '--config_vars', type=str, help='config(dev/prod/local or file_path)')

    return parser.parse_args()


def main():
    """
    Upgrades the current database schema to the latest version, also installs the uuid extensions.
    """
    print('Database Migrate Up Command')
    args = parse_args()
    util.source_config_vars(args.config_vars)
    paths = util.get_project_paths()
    alembic_path = paths['db'] / 'alembic.ini'
    migrations_path = paths['db'] / 'alembic_migrations'
    alembic_config = Config(alembic_path)
    alembic_config.set_main_option('sqlalchemy.url', util.get_db_str())
    alembic_config.set_main_option('script_location', str(migrations_path))
    print('Installing DB Extensions')
    db_util.install_db_extensions()
    print('Installed db extensions')
    print('Updating Database Schemas')
    command.upgrade(alembic_config, 'head')
    print('Updated database schemas')


if __name__ == '__main__':
    main()
