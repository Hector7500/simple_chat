import os
import shlex
import subprocess
from pathlib import Path


def get_project_paths(build_path=None):
    app_path = Path(os.path.dirname(os.path.realpath(__file__)))

    project_path = app_path.parent
    output_path = project_path / 'output'
    db_path = project_path / 'simple_chat' / 'db'

    if not build_path:
        build_path = project_path / 'build'

    else:
        build_path = Path(build_path)

    paths = {
        'script': project_path / 'scripts' / 'build',
        'project': project_path,
        'build': build_path,
        'output': output_path,
        'db': db_path
    }

    return paths


def source_config_vars(file_path):
    paths = get_project_paths()

    if file_path:

        ev_path = paths['project'] / 'config' / 'env_vars' / f'{file_path}.sh'

        source_env_vars(str(ev_path))

        return dict(os.environ)

    return {}


def source_env_vars(file_path):
    command = shlex.split(f"env -i bash -c 'source {file_path} && env'")
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)

    for line in proc.stdout:
        line = line.decode('utf-8')
        values = line.strip().split('=')
        os.environ[values[0]] = values[1]

    proc.communicate()
