import logging
logging.basicConfig(level=logging.DEBUG)

from testbox import create_app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from testbox.commands import manager
        manager.app = app
        manager.run()
