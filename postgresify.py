from os import environ

from dj_database_url import config


# Some constant globals that Heroku uses.
DEFAULT_URL = 'DATABASE_URL'
SHARED_URL = 'SHARED_DATABASE_URL'


def postgresify():
    """Return a fully configured Django ``DATABASES`` setting. We do this by
    analyzing all environment variables on Heroku, scanning for postgres DBs,
    and then making shit happen, duh.

    Returns a fully configured databases dict.
    """
    databases = {}

    # If the special ``DATABASE_URL`` variable is set, use this as the
    # 'default' database for Django.
    if environ.get(DEFAULT_URL, ''):
        databases['default'] = config()

    # If there is a legacy ``SHARED_DATABASE_URL`` variable set, assign this
    if environ.get(SHARED_URL, '') and databases.get('default', '') != config(env=SHARED_URL):
        databases['SHARED_DATABASE'] = config(env=SHARED_URL)

    # Analyze all environment variables looking for databases:
    for key in environ.keys():

        # If this is a Heroku PostgreSQL database:
        if key.startswith('HEROKU_') \
                and 'POSTGRESQL' in key \
                and key.endswith('_URL') \
                and databases.get('default', '') != config(env=key):

            # Generate a human-friendly database name:
            db_name = key.split('_')
            db_name.remove('HEROKU')
            db_name.remove('POSTGRESQL')
            db_name.remove('URL')
            db_name = '_'.join(db_name)

            databases[db_name] = config(env=key)

    return databases
