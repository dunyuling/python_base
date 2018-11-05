import urllib3
import chardet

http_pool = urllib3.PoolManager()


resp = http_pool.request('get','https://en.wikipedia.org/robots.txt')
encode_type = chardet.detect(resp.data)
#print(encode_type)
print(resp.data.decode("utf-8"))

"""
fh = open('robots','w')
fh.write(resp.data)
fh.close()
"""
