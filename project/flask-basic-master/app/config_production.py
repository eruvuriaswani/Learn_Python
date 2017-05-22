from .config import Config


class ConfigPrivate(Config):
    CSRF_SESSION_KEY = "NjFjZTllOTM5YzRhYjcxNDNlOGE1NWM4"
    SECRET_KEY = "ufdjYJHRRItHt0gXSa7N9GScfV83Vo2n8SZQ6ec3cg="

    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    THREADS_PER_PAGE = 2

    MAIL_ADMINS = ['javier.ramos@ikeasi']
    MAIL_USERNAME = 'javier.ramos@ikeasi.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '“WODEN admin” <noreply@ikeasi.com>'
    MAIL_SERVER = 'smtp.ikeasi.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
