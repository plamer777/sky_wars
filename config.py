class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://$DB_USER:$DB_PASS@$DB_HOST/$DB_NAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
