import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SKIP_FILE_TYPE = ['json', 'js', 'html', 'css', 'png', 'jpg', 'mpg', 'gif',
                  'html', 'xml', 'woff?v=4.2.0', 'ico', 'woff']
UPLOAD_FOLDER = os.path.join(basedir, "pub", "upload")
ALLOWED_EXTENSIONS = set(['txt', 'har', 'json'])
