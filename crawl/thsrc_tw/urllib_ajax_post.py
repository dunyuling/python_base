from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request('https://www.thsrc.com.tw/tw/TimeTable/Search')

postData = parse.urlencode([
    ('StartStation','2f940836-cedc-41ef-8e28-c2336ac8fe68'),
    ('EndStation','977abb69-413a-4ccf-a109-0272c24fd490'),
    ('DepartueSearchDate','2018/09/20'),
    ('DepartueSearchTime','05:30'),
    ('SearchType','S')
])
#print(postData)

req.add_header('Content-Type','application/x-www-form-urlencoded')
req.add_header('Host','www.thsrc.com.tw')
req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
resp = urlopen(req, data = postData.encode('utf-8'))

fh = open('twgt.html','w')
fh.write(resp.read().decode('utf-8'))
fh.close()
