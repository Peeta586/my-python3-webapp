#!/usr/bin/env python
# encoding: utf-8

#Set logging to print information not error.
import logging
logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<hl> Hello!</hl>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop =loop)
    app.router.add_route('GET','/',index)
    #assert isinstance(app.make_handler, object)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


