# ! /usr/bin/env python
# -*- coding: utf-8 -*- 

# 导入python内置的WSGI server
from wsgiref.simple_server import make_server

def application (environ, start_response):

    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)  # 由于下面将Content-Type设置为text/plain，所以`\n`在浏览器中会起到换行的作用

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

# 实例化WSGI server
httpd = make_server (
    '127.0.0.1', 
    8051, # port
    application # WSGI application，此处就是一个函数
)

# handle_request函数只能处理一次请求，之后就在控制台`print 'end'`了
httpd.handle_request()

print 'end'
