#!/usr/bin/env python
# encoding: utf-8

import ORM
import app
from models import User, Blog, Comment
import asyncio,aiomysql

async def test():
    await ORM.create_pool(loop, user='lshm', password='558866', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

for x in test():
    print("list")



