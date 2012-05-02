# django-heroku-postgresify

Automatic Django database configuration on Heroku.


![What if configuring PostgreSQL is really easy?](https://github.com/rdegges/django-heroku-postgresify/raw/master/assets/postgresify.jpg)


## Install

To install ``django-heroku-postgresify``, simply run
``pip install django-heroku-postgresify`` and you'll get the latest version
installed automatically.


## Usage

Modify your Django ``settings.py`` file, and set:

``` python
from postgresify import postgresify

DATABASES = postgresify()
```

That's it.

Depending on the Heroku PostgreSQL databases you've got installed, your
``DATABASES`` configuration will automatically be setup to use them.

For example, let's assume you've got the following environment variables set on
Heroku (you can view the list of all environment variables by running ``heroku
config``):

- ``HEROKU_POSTGRESQL_BLUE_URL``
- ``HEROKU_POSTGRESQL_RED_URL``
- ``HEROKU_SHARED_POSTGRESQL_RED_URL``
- ``SHARED_DATABASE_URL``
- ``DATABASE_URL``

Your ``DATABASES`` setting would be:

``` python
DATABASES = {
    'default': {
        # DATABASE_URL configs here
    },
    'SHARED': {
        # SHARED_DATABASE_URL configs here
    },
    'BLUE': {
        # HEROKU_POSTGRESQL_BLUE_URL configs here
    },
    'RED': {
        # HEROKU_POSTGRESQL_RED_URL configs here
    },
    'SHARED_RED': {
        # HEROKU_SHARED_POSTGRESQL_RED_URL configs here
    },
}
```


## References

If you're confused, you should probably read:

- [Heroku's Getting Started Guide](http://devcenter.heroku.com/articles/django)
- [Deploy Django's PostgreSQL Section](http://www.deploydjango.com/postgresql/index.html)


## Tests

[![Build Status](https://secure.travis-ci.org/rdegges/django-heroku-postgresify.png?branch=master)](http://travis-ci.org/rdegges/django-heroku-postgresify)

Want to run the tests? No problem:

``` bash
$ git clone git://github.com/rdegges/django-heroku-postgresify.git
$ cd django-heroku-postgresify
$ python setup.py develop
...
$ pip install -r requirements.txt  # Install test dependencies.
$ nosetests
.............
----------------------------------------------------------------------
Ran 13 tests in 0.166s

OK
```
