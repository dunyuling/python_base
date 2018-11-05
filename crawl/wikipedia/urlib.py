from urllib.request import urlopen
from urllib.request import Request
import chardet

req = Request('https://en.wikipedia.org/robots.txt')

resp = urlopen(req)
buf = resp.read()
encode_type = chardet.detect(buf)
print(encode_type)
#print(buf.decode('utf-8'))

"""
fh = open('robots','w')
fh.write(resp.read().decode('utf-8'))
#fh.write(resp.read())
fh.close()
"""
