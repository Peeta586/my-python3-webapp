#!/usr/bin/env python
# encoding: utf-8

import logging
logging.basicConfig(level=logging.INFO)

import asyncio

#配置python3.5环境，需要更改Pycharm中的（PyCharm菜单下）Perferences，和(files菜单下)Default Setting两个设置。
#注意，主要是Perferences的更改。

#create a threads pool
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.INFO('create database connection pool...')
    global __pool
    __pool  = yield from aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        password=kw['password'],
        db =kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize =kw.get('mazsize',10),
        minsize=kw.get('minsize',1),
        loop =loop
    )

#create some general operational functions

@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('row returned :%s' % len(rs))
        return rs




