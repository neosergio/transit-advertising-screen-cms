"""
Environment common functions.

Created by Sergio Infante.
"""

from os import environ


def env(variable, default_value):
    '''
    Return a value from environments variables, if not exists returns default_value
    '''
    if variable in environ:
        return environ[variable]
    else:
        return default_value
