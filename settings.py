import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    default='postgresql://appuser:password@localhost:5432/big3logger_db' #only local
    )
