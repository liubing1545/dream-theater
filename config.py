# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.live.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    THEATER_MAIL_SUBJECT_PREFIX = '[TattooMe]'
    THEATER_MAIL_SENDER = 'TattooMe Admin <tattoome@example.com>'
    THEATER_ADMIN = os.environ.get('TATTOOME_ADMIN')
    THEATER_POSTS_PER_PAGE = 20
    THEATER_FOLLOWERS_PER_PAGE = 50
    THEATER_COMMENTS_PER_PAGE = 30

    #七牛access-key和secret-key
    QINIU_ACCESS_KEY = os.environ.get('QINIU_ACCESS_KEY')
    QINIU_SECRET_KEY = os.environ.get('QINIU_SECRET_KEY')

    #七牛空间名
    PIC_BUCKET = os.environ.get('PIC_BUCKET')
    #七牛域名
    PIC_DOMAIN = os.environ.get('PIC_DOMAIN')

    #网盘存储空间及域名
    DISK_BUCKET = os.environ.get('DISK_BUCKET')
    DISK_DOMAIN = os.environ.get('DISK_DOMAIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
