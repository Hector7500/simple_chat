import subprocess

import sys


def main():
    cmds = 'virtualenv simple_chat_env'.split()
    subprocess.run(cmds, check=True)
    sys.exit(0)


if __name__ == '__main__':
    main()
