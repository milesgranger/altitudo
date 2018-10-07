# -*- coding: utf-8 -*-

"""Console script for altitudo."""
import sys
import click

from altitudo import altitudo


@click.command('altitudo')
@click.argument('lat', type=click.FLOAT)
@click.argument('lon', type=click.FLOAT)
@click.option('--feet', default=False)
def main(lat, lon, feet=False):
    """Console script for altitudo."""
    elevation = altitudo(lat, lon, feet)
    click.echo(elevation)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
