class Config:
    SECRET_KEY = '12345'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'tienda'

config={
    'development':DevelopmentConfig
}