import aiohttp
import asyncio
import datetime
from aiohttp import web

async def clock_handler(request):
    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="1">
    </head>
    <body>
        <h1>Current Time</h1>
        <p>{}</p>
    </body>
    </html>
    """.format(datetime.datetime.now())
    return web.Response(text=html, content_type='text/html')

async def init_app():
    app = web.Application()
    app.router.add_get('/', clock_handler)
    return app

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    web.run_app(app, host='0.0.0.0', port=8080)