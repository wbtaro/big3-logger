import logging
import sys

from flask import request, abort, jsonify

from . import app
from .models import Genre, TrainingLog

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

@app.route('/genres')
def get_genres():
    genres = Genre.query.all()
    return jsonify({
        'genres': [genre.name for genre in genres]
    })

# Default port:
if __name__ == '__main__':
    app.run()
