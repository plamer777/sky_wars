class FlaskConfig:
    """The configuration class for Flask application"""
    SQLALCHEMY_DATABASE_URI = (
        'postgresql+psycopg2://plamer777:LegatCalibra47960805@postgres' 
        '/skywars_data')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET = 'plamer_password'
    JWT_ALGO = 'HS256'

    HASH_SALT = b'calibra_salt'
    HASH_ALGO = 'sha256'
    HASH_ITERATIONS = 1052
