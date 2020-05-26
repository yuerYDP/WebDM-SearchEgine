# encoding=utf-8

import urllib
import urllib.request
from urllib.parse import urlparse, urljoin
import re
import os
import requests
from bs4 import BeautifulSoup
import time

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # response = requests.get(url)
        # response.encoding = 'utf-8'
        # return response.text
        response = urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

def match_pattern(html):
    suffix = html.split('/')[-1]
    r = re.match("\d+\.html", suffix)
    if r is not None:
        return suffix
    else:
        return None


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=True)
        for link in links:
            new_url = link['href']
            suffix = match_pattern(new_url)
            if suffix is not None:
                new_full_url = urljoin(page_url, suffix) + '/'
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        content_node = soup.find_all(class_="content_detail")
        if len(content_node) > 0:
            for index, c in enumerate(content_node):
                str = c.get_text().strip()
                content_node[index] = str
            content = "".join(content_node)
            res_data['content'] = content
        else:
            res_data['content'] = 'null'

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8"')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

def write_data(data):
    data_dir = os.path.join(os.path.abspath(os.curdir), 'crawl_data')
    file_name = data['url']
    if file_name[-1] == '/':
        file_name = file_name[:-1]
    file_name = file_name.split('/')[-1]
    print(file_name)
    if file_name.split('.')[-1] == 'html':
        file_name = file_name.split('.')[0]
        file_path = os.path.join(data_dir, file_name+'.txt')
        print(file_path)
        with open(file_path, 'w') as f:
            f.write(data['content'])

class Spider(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("crawl {}: {}".format(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                write_data(new_data)

                if count > 3000:
                    break

                count = count + 1
            except:
                print("crawl_fail")
                time.sleep(60)
                print("sleep 30s")

if __name__ == "__main__":
    root_url = "https://www.biqugela.com/book_29782/"
    obj_spider = Spider()
    obj_spider.crawl(root_url)