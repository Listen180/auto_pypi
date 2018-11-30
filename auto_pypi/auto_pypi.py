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

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
                      help='The person to greet.')
def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
            for x in range(count):
                        click.echo('Hello %s!' % name)




















@click.command()
@click.option(
    'real_pypi', '--real', '-r',
    default=False,
    is_flag=True,
    help="Set to use the real PyPi index. ",
    required=False,
)
@click.argument('text', nargs=-1, type=click.STRING, required=True)
def main(from_lang, to_lang, provider, secret_access_key, output_only, text):
    """
    Python command line tool to setup Python package automatically. 
    \b
    Example:
    \b
    \t $ autopypi -r 
    \t 
    """
    text = ' '.join(text)

    kwargs = dict(from_lang=from_lang, to_lang=to_lang, provider=provider)
    if provider != DEFAULT_PROVIDER:
        kwargs['secret_access_key'] = secret_access_key

    translator = Translator(**kwargs)
    translation = translator.translate(text)
    if sys.version_info.major == 2:
        translation = translation.encode(locale.getpreferredencoding())

    if real_pypi:
        click.echo("! Using R-E-A-L PyPi index ! ")
    else:
        click.echo("! Using TEST PyPi index ! ")


    click.echo('\nTranslation: {}'.format(translation))
    click.echo('-' * 25)
    click.echo('Translated by: {}'.format(translator.provider.name))
