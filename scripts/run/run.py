import argparse
import subprocess
import sys

from scripts import util


def parse_args():
    parser = argparse.ArgumentParser(description='Run app.')
    parser.add_argument('-c', '--config_vars', type=str, help='environment(dev/prod)')

    return parser.parse_args()


def main():
    print('Run Application')
    args = parse_args()
    env = util.source_config_vars(args.config_vars)
    cmds = f'flask run -h 0.0.0.0 -p {env["FLASK_PORT"]} --no-reload'.split()
    subprocess.run(cmds, check=True)

    sys.exit(0)


if __name__ == '__main__':
    main()
