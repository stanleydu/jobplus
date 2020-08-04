#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@version: v1.0
@author = pdu
@license: pdu Licence 
@contact: 1090416@qq.com
@project = jobplus
@file: app.py
@create_time = 2020/8/44:28 下午
"""
from flask import Flask
from jobplus.config import configs
from flask_migrate import Migrate
from flask_login import LoginManager
from jobplus.models import db, User

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprint(app)

def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'
