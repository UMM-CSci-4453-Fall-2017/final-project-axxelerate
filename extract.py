from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field

class url_item(Item):
    url= Field()


class axxelerate_spider(CrawlSpider):
    name = 'axxelerate'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse', follow=True),)

    def parse(self,response):
        item = url_item()
        item['url'] = []
        for link in LxmlLinkExtractor(allow=(self.allowed_domains),deny = ()).extract_links(response):
            if 'en.wikipedia.org' in link.url:
                item['url'].append(link.url)
        return item