class Config():
    DEBUG = False
    TESTING = False

    USER_APP_NAME = 'Application'

    # Flask-User settings
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
    USER_ENABLE_CONFIRM_EMAIL = False  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_EMAIL = True  # Register with Email
    USER_ENABLE_REGISTRATION = False  # Allow new users to register
    USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_ENABLE_USERNAME = True  # Register and Login with username

    # end points
    USER_AFTER_CHANGE_PASSWORD_ENDPOINT      = ''
    USER_AFTER_CHANGE_USERNAME_ENDPOINT      = ''
    USER_AFTER_CONFIRM_ENDPOINT              = ''
    USER_AFTER_FORGOT_PASSWORD_ENDPOINT      = ''
    USER_AFTER_LOGIN_ENDPOINT                = ''
    USER_AFTER_LOGOUT_ENDPOINT               = 'user.login'
    USER_AFTER_REGISTER_ENDPOINT             = ''
    USER_AFTER_RESEND_CONFIRM_EMAIL_ENDPOINT = ''
    USER_AFTER_RESET_PASSWORD_ENDPOINT       = ''
    USER_INVITE_ENDPOINT                     = ''

class ConfigDev(Config):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    SECRET_KEY = ('\xcc\xc1\xae4\xb3\xd7\xc5\xc3\x10\xcd^\x0f\xab\xca,!0\xe1'
                  '\xa6\xa1\xf2\xdeB\x1f')

    import os
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app-devel.db'

    MAIL_ADMINS = ['javier.ramos@ikeasi']
    MAIL_USERNAME = 'javier.ramos@ikeasi.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '“WODEN admin” <noreply@ikeasi.com>'
    MAIL_SERVER = 'smtp.ikeasi.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
