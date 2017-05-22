from hangman.app import create_app, create_db


app = create_app()


if __name__ == '__main__':
    create_db(app)
    app.run()


# Webpages
#  index/root view
#  login
#  game page
#  ability to log out
#  if time: win/loss records per user view

# Functions
#  Database handler
#  login
#  logout
#  connection/session manager to update clients of the game status

