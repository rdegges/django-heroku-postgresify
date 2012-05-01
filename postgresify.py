from os import environ

from dj_database_url import config


def postgresify():
    """Return a fully configured Django ``DATABASES`` setting. We do this by
    analyzing all environment variables on Heorku, scanning for postgres DBs,
    and then making shit happen, duh.

    Returns a fully configured databases dict.
    """
    databases = {}

    if environ.get('DATABASE_URL', ''):
        databases['default'] = config()

    for key in environ.iterkeys():

        # If this is a shared database:
        if key == 'SHARED_DATABASE_URL' and databases.get('default', '') != config(env=key):
            databases['SHARED'] = config(env=key)

        # If this is a paid database (or a fancy new shared database):
        elif (key.startswith('HEROKU_') and 'POSTGRESQL' in key and key.endswith('_URL')) and databases.get('default', '') != config(env=key):
            databases[key.split('_')[-2]] = config(env=key)

    return databases
