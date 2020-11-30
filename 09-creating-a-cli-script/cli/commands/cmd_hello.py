import subprocess

import click


@click.command()
@click.option('--name', default='World',
              help='Enter your name.')
def cli(name):
    """
    Say hello to the entered name.

    :param name: name to say hello to

    :return: Subprocess call result
    """

    cmd = 'echo Hello {0}!'.format(name)
    return subprocess.call(cmd, shell=True)
