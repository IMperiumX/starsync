"""Console script for starsync."""
import sys

import asyncio
from timeit import default_timer

import click

from .sync_unstart_repos import unstar_repos_async


@click.command()
def main(args=None):
    start = default_timer()
    asyncio.run(unstar_repos_async())
    elapsed = default_timer() - start
    click.echo(f"Elapsed Time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
