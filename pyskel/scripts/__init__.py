# Skeleton of a CLI

import click

import pyskel


@click.command('pyskel')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(pyskel.has_legs)
