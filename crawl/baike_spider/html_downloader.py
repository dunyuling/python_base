import urllib3
import chardet
from urllib3.exceptions import InsecureRequestWarning

class HtmlDownloader(object):
    def __init__(self):
        self.http_pool = urllib3.PoolManager() 
        # 禁用安全请求警告
        urllib3.disable_warnings(InsecureRequestWarning)

    def download(self, url):
        if url is None:
            return None

        resp = self.http_pool.request('get', url)   
        if resp.status != 200:
            return None
        return resp.data
