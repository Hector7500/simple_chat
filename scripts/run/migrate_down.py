import argparse

from alembic.config import Config  # type: ignore
from alembic import command  # type: ignore

from simple_chat import util


def parse_args():
    parser = argparse.ArgumentParser(description='Migrate the DB down.')
    parser.add_argument('-c', '--config_vars', type=str, help='config(dev/prod/local or file_path)')

    return parser.parse_args()


def main():
    """
    Once this downgrade is run, the database downgrades the schema into the previous version.
    """
    print('Migrate Down')
    args = parse_args()
    util.source_config_vars(args.config_vars)
    paths = util.get_project_paths()
    alembic_path = paths['db'] / 'alembic.ini'
    migrations_path = paths['db'] / 'alembic_migrations'
    alembic_config = Config(alembic_path)
    alembic_config.set_main_option('sqlalchemy.url', util.get_db_str())
    alembic_config.set_main_option('script_location', str(migrations_path))
    print('Migrating Down Table Schemas One Version')
    command.downgrade(alembic_config, "-1")


if __name__ == '__main__':
    main()
