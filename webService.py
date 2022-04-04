import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8000

if len(sys.argv) == 2 and sys.argv[1].isnumeric(): port = int(sys.argv[1])
else:
    print ("uso python websever.py{port}")
    print (f">>>>> por defecto asigna puerto {port}")

os.chdir('.')

with HTTPServer(server_address=('',port),RequestHandlerClass=CGIHTTPRequestHandler)as httpd:

    print(f"\n sirviendo en puerto: {port}")
    httpd.serve_forever()