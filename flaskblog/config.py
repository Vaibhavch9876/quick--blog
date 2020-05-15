import os


class Config:
    SECRET_KEY = 'baa80ced1a8e2ee4168e2069e3e8512b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FLASK_MAIL')
    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASS')