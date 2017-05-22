

class DevConfiguration:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://John:Richter@localhost/hangman'
    SQLALCHEMY_ECHO = True
    CSRF_ENABLED = True
    SECRET_KEY = "_Let'sK3epThi$Super-5ekret*1nf"
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'Some[r4zy1mpor7ed_$alt'
    SECURITY_CONFIRM_SALT = 'Some_non-defaul7.$alt'
    SECURITY_RESET_SALT = 'Some_non-defaul7^Res3t.$alt'
    SECURITY_LOGIN_SALT = 'Some_non-defaul7,L0Gin$alt'
    SECURITY_REMEMBER_SALT = 'Some_non-defaul7,Rem3mber&$alt'
    SECURITY_REGISTERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
