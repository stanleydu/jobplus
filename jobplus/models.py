#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@version: v1.0
@author = pdu
@license: pdu Licence 
@contact: 1090416@qq.com
@project = jobplus
@file: models.py
@create_time = 2020/8/44:29 下午
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import url_for

db = SQLAlchemy()

class Base(db.Model):
    pass

class User(Base, UserMixin):
    pass