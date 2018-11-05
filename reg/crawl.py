import urllib3
import chardet
import re
import datetime

time_pattern = '%Y.%m.%d-%H:%M:%S'

from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)

http_pool = urllib3.PoolManager()
print('抓取开始:',datetime.datetime.now().strftime(time_pattern))
print('抓取网页开始')
resp = http_pool.request('get','https://www.imooc.com/course/list')
print('抓取网页结束')

print('分析网页字符编码')
encode_type = chardet.detect(resp.data)
print('解码网页内容')
buf = resp.data.decode(encode_type['encoding'])

print('提取图片地址')
listurl = re.findall(r'src=.+\.jpg',buf)

def replace_src(source):
    return re.sub('src="','https:', source)


print('抓取图片内容开始')
i = 0
for x in listurl:
    url = replace_src(x) 
    f = open('jpg/'+str(i)+'.jpg','bw')
    img_resp = http_pool.request('get',url)   
    f.write(img_resp.data)
    f.close()
    i+=1 
print('抓取图片内容结束')
print('抓取结束:',datetime.datetime.now().strftime(time_pattern))
