import url_manager
import html_downloader
import html_parser
import html_outputer
import utils

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer() 

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url) 
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('crawl %d : %s ' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data) 

                if count == 1000:
                    break

                count += 1
            except Exception as e:
                print('crawl failed')
                print(e)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    print('爬虫开始:', utils.get_now())
    obj_spider.crawl(root_url)
    print('爬虫结束:', utils.get_now())
