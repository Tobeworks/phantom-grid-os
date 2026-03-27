#!/usr/bin/env python3
"""
Phantom Grid CLI
The operating layer for the world's first 100% code-based music label.

Usage:
  ./pg generate <release-folder-path>               — scan audio, write release.json
  ./pg validate <release-folder-path>               — validate against schema
  ./pg validate <release-folder-path> --generate-md — validate + write release.md draft
  ./pg social   <release-folder-path>               — render social media assets
  ./pg social   <release-folder-path> --format reel — square | reel | carousel | all
  ./pg push     <release-folder-path>               [coming]
"""

import click
from commands.validate import validate_release
from commands.generate import generate_release
from commands.social   import generate_social

@click.group()
@click.version_option(version='0.3.0', prog_name='phantom-grid')
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

@cli.command()
@click.argument('release_path', type=click.Path(exists=True))
@click.option('--format', 'output_format', default='square',
              type=click.Choice(['square', 'reel', 'all']),
              help='Output format. Default: square.')
@click.option('--duration', default=30, show_default=True,
              help='Clip length in seconds.')
@click.option('--init', is_flag=True, default=False,
              help='Write social.json config skeleton and exit.')
def social(release_path, output_format, duration, init):
    """Render social media assets for a release. Use --init to configure first."""
    generate_social(release_path, fmt=output_format,
                    duration=duration, init=init)

# Future commands:
# @cli.command()
# def push(): ...

if __name__ == '__main__':
    cli()
