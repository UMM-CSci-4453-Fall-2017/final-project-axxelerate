from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field

class url_item(Item):
    url= Field()


class axxelerate_spider(CrawlSpider):
    name = 'axxelerate'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self,response):
        item = url_item()
        item['url'] = []
        for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
            item['url'].append(link.url)
        return item