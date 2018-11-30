#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-30 13:30
# * Last modified : 2018-11-30 13:30
# * Filename      : main.py
# * Description   : 
# *********************************************************

import sys
import os
import click


HERE = os.path.dirname(os.path.abspath(__file__))

print(HERE)

@click.command()
@click.option(
    'real_pypi', '--real', '-r',
    default=False,
    is_flag=True,
    help="Set to use the real PyPi index. ",
    required=False,
)
@click.option(
    'pkg_name', '--name', '-n',
    help="Set the package name. ",
    required=True,
)
@click.option(
    'pkg_version', '--version', '-v',
    help="Set the package version number. ",
    required=True,
)
@click.argument('pkg_dir', nargs=1, type=click.STRING, required=True)
#@click.argument('pkg_name', nargs=1, type=click.STRING, required=True)
def main(pkg_dir, pkg_name, pkg_version, real_pypi):
    """
    Python command line tool to setup Python package automatically. 
    \b
    Example:
    \b
    \t $ autopypi your-package-root-directory -n package_name -v package_version -r
    \t 
    """
    click.echo('')
    click.echo(' Preparing package {} (v{}) ... '.format(pkg_name, pkg_version))
    click.echo('')

    if real_pypi:
        click.echo("    ! Using REAL PyPi index ! ")
    else:
        click.echo("    ! Using TEST PyPi index ! ")

