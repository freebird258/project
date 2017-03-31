# ! /usr/bin/env python
# -*- coding: utf-8 -*- 

from wsgiref.simple_server import make_server

def application(environ, start_response):

#    response_body = [
#        '%s: %s' % (key, value) for key, value in sorted(environ.items())
#    ]
#    response_body = '\n'.join(response_body)

    response_body = [
        'The Beggining\n',
        '*' * 30 + '\n',
        '\n' + '*' * 30 ,
        '\nThe End'
    ]

    # 求Content-Length
    content_length = sum([len(s) for s in response_body])

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(content_length))
    ]

    start_response(status, response_headers)
    return response_body

httpd = make_server('localhost', 8051, application)
httpd.handle_request()
