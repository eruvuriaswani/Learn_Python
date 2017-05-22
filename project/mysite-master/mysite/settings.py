import os
import logging
from datetime import timedelta

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s: %(message)s',
)

PROJECT_NAME = ''
# Major.Minor.Revision
PROJECT_VERSION = '1.0'
PROJECT_COMPANY = ''
PROJECT_AUTHOR = ''
PROJECT_COPYRIGHT = PROJECT_COMPANY
PROJECT_DESCRIPTION = 'A tool for testing based on webpage'



# Cookie secret
SECRET_KEY = 'dX6mg0jx0y`8(F_|Cp(#zUQTSAX_y<Q0%^W*#Q7<Wwyb2$^9DB4f<J>7Q~*#{&F~'

# Cache prefix
CACHE_PREFIX = '%s_%s_' % (PROJECT_NAME, PROJECT_VERSION)

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_ECHO = False
SQLALCHEMY_RECORD_QUERIES = False
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 2 * 60 * 60
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

#WTForms
WTF_CSRF_ENABLED = False

