class Config():
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    PORT = 5000
    DEBUG = True
    DRIVER = ''
    SERVER = ''
    DATABASE = 'Biblioteca'
    USERNAME = ''
    PASSWORD = ''



configDic = {
    'development': DevelopmentConfig,
}


#La Pagina esta en este link
# localhost:5000/user/