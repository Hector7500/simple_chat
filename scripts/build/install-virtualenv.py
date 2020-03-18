import subprocess
import sys


def main():
    # Script vars
    print('pip installing virtualenv')
    cmds = 'pip install virtualenv'.split()
    subprocess.run(cmds, check=True)
    sys.exit(0)


if __name__ == '__main__':
    main()
