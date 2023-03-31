class FlaskConfig:
    """The configuration class for Flask application"""
    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2:///$DB_USER:$DB_PASS@$DB_HOST/$DB_NAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET = '$JWT_SECRET'
    JWT_ALGO = 'HS256'

    HASH_SALT = b'$HASH_SALT'
    HASH_ALGO = 'sha256'
    HASH_ITERATIONS = 1052
