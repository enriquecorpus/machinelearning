from icrawler.builtin import GoogleImageCrawler
import os

keyword_ = input('Type keyword you want to download: ')
google_crawler = GoogleImageCrawler(
    storage={'root_dir': '{f}/{keyword}/'.format(f=os.getcwd(), keyword=keyword_)}, parser_threads=2,
    downloader_threads=4)
#google_crawler.session.verify = False
google_crawler.crawl(keyword=keyword_, max_num=100, min_size=(100, 100), max_size=(200, 200))
