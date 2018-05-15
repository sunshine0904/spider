#!/usr/bin/env python
# coding=utf-8

class HtmlPaser(object):

    def _get_new_urls(self,page_url,soup):
        links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
        for lin in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}

        res_data['url'] = page_url

        title_node = soup.find('dd',class_="*").find("h1")
        res_data['title'] = titile_node.get_text()

        summary_node = soup.find('div',class_="*")
        res_data['summary'] = summary_node,get_text()

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html_parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
