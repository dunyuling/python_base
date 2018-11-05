import urllib3
import chardet
from bs4 import BeautifulSoup

http_pool = urllib3.PoolManager()
resp = http_pool.request('get','https://baike.baidu.com/item/Python/407313')
encode_type = chardet.detect(resp.data)
print(type(resp.data))
buf = resp.data.decode(encode_type['encoding'])
fh = open('txt','w')
print(buf, file=fh)
fh.close()
soup = BeautifulSoup(resp.data,'html.parser')

