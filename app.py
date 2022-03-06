import logging
import sys

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Set Loggings.
#----------------------------------------------------------------------------#
logger = logging.getLogger(__name__)

if app.debug:
    handler = logging.StreamHandler(sys.stdout)
else:
    handler = logging.FileHandler('error.log')

handler.setFormatter(
    logging.Formatter(
      '%(asctime)s %(levelname)s: \
      %(message)s [in %(pathname)s:%(lineno)d]'
    )
)

handler.setLevel(logging.WARNING)
logger.addHandler(handler)


#----------------------------------------------------------------------------#
# Define Routes.
#----------------------------------------------------------------------------#
@app.route('/')
def index():
    return jsonify({
        'app': 'big3-logger-api'
    })

# Default port:
if __name__ == '__main__':
    app.run()
