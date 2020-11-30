import subprocess

import click


@click.command()
@click.argument('name', default='World')
def cli(name):
    """
    Says hi using the entered argument.

    :param path: name to say hi to

    :return: Subprocess call result
    """
    cmd = 'echo Hi {0}!'.format(name)
    return subprocess.call(cmd, shell=True)
