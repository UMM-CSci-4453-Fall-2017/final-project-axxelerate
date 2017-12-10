from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field

class url_item(Item):
    url= Field()
    keywords = Field()

class axxelerate_spider(CrawlSpider):
    name = 'axxelerate'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
    rules = (Rule(LxmlLinkExtractor(allow=(allowed_domains)), callback='parse_obj', follow=True),)

    def parse_obj(self,response):
        item = url_item()
        item['url'] = response.url
        item['keywords'] = []
        tags = ["h1", "h2", "h3", "h4", "h5", "h6", "title", "article", "div",
                "blockquote", "td", "li", "a", "p", "span", "strong", "bold"]
        for tag in tags:
            item['keywords'].append(response.xpath("//%s/text()" % (tag)).extract())
        return item
