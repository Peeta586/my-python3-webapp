#!/usr/bin/env python
# encoding: utf-8
from models import User, Blog, Comment

u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
u.save()
