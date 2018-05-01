import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    BOOTSTRAP_SERVE_LOCAL= True
    SECRET_KEY="Hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data-dev.sqlite")
    BOARD_COMMENTS_PER_PAGE = os.environ.get("FLASKY_POSTS_PER_PAGE") or 8

class TestingConfig(Config):
    TESTING = True    
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data-test.sqlite")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data.sqlite")

config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "productin":ProductionConfig,
    "default":DevelopmentConfig
}