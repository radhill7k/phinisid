#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ["KIVY_NO_ARGS"] = "1"

import click

from phinisid.phinisid import phinisidApp


@click.command()
@click.option(
    '-l', '--language', help='Default language of the App', default='en',
    type=click.Choice(['en', 'es', 'de', 'fr'])
)
def main(language):
    """Run phinisidApp with the given language setting.
    """
    phinisidApp(language).run()
