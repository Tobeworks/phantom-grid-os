#!/usr/bin/env python3
"""
Phantom Grid CLI
The operating layer for the world's first 100% code-based music label.

Usage:
  ./pg generate <release-folder-path>              — scan audio, write release.json
  ./pg validate <release-folder-path>              — validate against schema
  ./pg validate <release-folder-path> --generate-md — validate + write release.md
  ./pg push <release-folder-path>                  [coming]
"""

import click
from commands.validate import validate_release
from commands.generate import generate_release

@click.group()
@click.version_option(version='0.2.0', prog_name='phantom-grid')
def cli():
    """Phantom Grid OS — label toolchain."""
    pass

@cli.command()
@click.argument('release_path', type=click.Path(exists=True))
def generate(release_path):
    """Scan audio folder and generate release.json skeleton."""
    generate_release(release_path)

@cli.command()
@click.argument('release_path', type=click.Path(exists=True))
@click.option('--generate-md', is_flag=True, default=False,
              help='Generate release.md draft if validation passes.')
def validate(release_path, generate_md):
    """Validate a release asset folder against the Phantom Grid schema."""
    validate_release(release_path, generate_md=generate_md)

# Future commands:
# @cli.command()
# def push(): ...

if __name__ == '__main__':
    cli()
