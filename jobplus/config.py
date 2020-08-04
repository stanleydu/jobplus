#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@version: v1.0
@author = pdu
@license: pdu Licence 
@contact: 1090416@qq.com
@project = jobplus
@file: config.py
@create_time = 2020/8/44:28 下午
"""
class BaseConfig(object):
    """配置基类"""
    SECRET_KEY = 'makesure to set a very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:drm2014!@localhost:3306/jobplus?charset=utf8'
    # SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    """生产环境配置"""
    pass


class TestingConfig(BaseConfig):
    pass



configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}