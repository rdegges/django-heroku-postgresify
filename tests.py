from os import environ
from unittest import TestCase

from postgresify import postgresify


class Postgresify(TestCase):

    def test_returns_empty_dict_if_no_dbs_are_available(self):
        self.assertEqual(postgresify(), {})

    def test_detects_database_url(self):
        environ['DATABASE_URL'] = 'postgres://abc:def@ec2-23-23-217-149.compute-1.amazonaws.com/xxx'
        self.assertTrue(postgresify()['default'])
        del environ['DATABASE_URL']

    def test_detects_shared_database(self):
        environ['SHARED_DATABASE_URL'] = 'postgres://abc:def@ec2-23-23-217-149.compute-1.amazonaws.com/xxx'
        self.assertTrue(postgresify()['SHARED_DATABASE'])
        del environ['SHARED_DATABASE_URL']

    def test_detects_heroku_postgres_shared_database(self):
        environ['HEROKU_SHARED_POSTGRESQL_RED_URL'] = 'postgres://abc:def@ec2-23-23-217-149.compute-1.amazonaws.com/xxx'
        self.assertTrue(postgresify()['SHARED_RED'])
        del environ['HEROKU_SHARED_POSTGRESQL_RED_URL']

    def test_detects_heroku_databases(self):
        environ['HEROKU_POSTGRESQL_TEAL_URL'] = 'postgres://abc:def@ec2-23-23-217-149.compute-1.amazonaws.com/xxx'
        self.assertTrue(postgresify()['TEAL'])
        del environ['HEROKU_POSTGRESQL_TEAL_URL']

    def test_doesnt_include_a_database_twice_if_it_is_set_as_default(self):
        environ['DATABASE_URL'] = 'postgres://abc:def@ec2-23-23-217-149.compute-1.amazonaws.com/xxx'
        environ['HEROKU_POSTGRESQL_AQUA_URL'] = 'postgres://abc:def@ec2-23-23-217-149.compute-1.amazonaws.com/xxx'
        self.assertFalse('AQUA' in postgresify())
        del environ['DATABASE_URL']
        del environ['HEROKU_POSTGRESQL_AQUA_URL']

