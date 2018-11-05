import urllib3
import json
import chardet
from urllib.parse import urlencode
import pprint

http_pool = urllib3.PoolManager()

data = {
    'DepartueSearchDate':'2018/09/20',
    'DepartueSearchTime':'05:30',
    'EndStation':'977abb69-413a-4ccf-a109-0272c24fd490', 
    'SearchType':'S', 
    'StartStation':'2f940836-cedc-41ef-8e28-c2336ac8fe68'}
encoded_args = urlencode(data)
print(encoded_args)

resp = http_pool.request(
    'post',
    'https://www.thsrc.com.tw/tw/TimeTable/Search?'+ encoded_args)

#print(resp.status)
encode_type = chardet.detect(resp.data)
buf = resp.data.decode(encode_type['encoding'])
pprint.pprint(buf)
"""
fh = open('twgt_urllib3','w')
fh.write(buf)
fh.close()
"""
