class FlaskConfig:
    """The configuration class for Flask application"""
    SQLALCHEMY_DATABASE_URI = (
        'postgresql+psycopg2://$POSTGRES_USER:$POSTGRES_PASSWORD@$DB_HOST' 
        '/$POSTGRES_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET = '$JWT_SECRET'
    JWT_ALGO = 'HS256'

    HASH_SALT = b'$HASH_SALT'
    HASH_ALGO = 'sha256'
    HASH_ITERATIONS = 1052
