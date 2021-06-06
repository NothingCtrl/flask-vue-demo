#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask_login

# mock database
users = {'demo': {'password': 'demo'}}

class User(flask_login.UserMixin):
    pass


