#!/usr/bin/env python3
# encoding: utf-8

__author__ = "Lishiming"
#这文件主要实现一些handle的基本处理函数，将一些重复的操纵过程封装，从而使得形成一个前端框架
import asyncio, os, inspect,logging,functools

from urllib import parse
from aiohttp import web
from apis import APIErorr

def get(path):
    '''
    Define decorator @get('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.warps(func)
        def wrapper(*args,**kw):
            return func(*args,**kw)
        wrapper.__method__ ='GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    '''
    Define decorator @post('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator