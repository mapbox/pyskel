# Skeleton of a CLI

import click

import pyskel

@click.command('pyskel', help="A Skeleton of a command line interface")
@click.argument('count', type=int)
def cli(count):
    for i in range(count):
        click.echo(pyskel.has_legs)
