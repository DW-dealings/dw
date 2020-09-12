import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Bloodborne115588##@localhost/exchel'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER", 'smtp.sendgrid.net')
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", 'apikey')
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", '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')
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", 'hakunamatata5515@gmail.com')