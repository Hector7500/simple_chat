import argparse

from alembic.config import Config  # type: ignore
from alembic import command  # type: ignore

from simple_chat import util


def parse_args():
    parser = argparse.ArgumentParser(description='Migrate the DB up.')
    parser.add_argument('-c', '--config_vars', type=str, help='config(dev)')
    parser.add_argument('-m', '--message', type=str, nargs='+', default="", help='migration message')

    return parser.parse_args()


def main():
    """
    Autogenerates migrations.
    """
    print('Generating Database Migration')
    args = parse_args()
    util.source_config_vars(args.config_vars)
    paths = util.get_project_paths()
    alembic_path = paths['db'] / 'alembic.ini'
    alembic_cfg = Config(alembic_path)
    alembic_cfg.set_main_option('sqlalchemy.url', util.get_db_str())
    new_msg = ' '.join(args.message)

    command.revision(alembic_cfg, autogenerate=True, message=new_msg)


if __name__ == '__main__':
    main()
