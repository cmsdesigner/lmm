# -*- coding: utf-8 -*-
import os


class BaseConfig(object):

    # Get app root path
    # ../../configs/config.py
    _basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    PROJECT = "lmm"
    DEBUG = False
    TESTING = False

    SECRET_KEY = '\x8137i\xd6\xc4X\xf4Y\xcf\xb3\x95M\xe4n\xbf\xd5\xb3\x18}l\x81\x03\xb5'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://lapiduzd@localhost:5432/lmm_dev'


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/lmm_test'

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('HEROKU_POSTGRESQL_CHARCOAL_URL')