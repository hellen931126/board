import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    BOOTSTRAP_SERVE_LOCAL= False
    SECRET_KEY= b'_5#y2L"F4Q8z\n\xec]/'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3306/board"
    BOARD_COMMENTS_PER_PAGE = os.environ.get("BOARD_COMMENTS_PER_PAGE") or 8
    

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/board"

config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}