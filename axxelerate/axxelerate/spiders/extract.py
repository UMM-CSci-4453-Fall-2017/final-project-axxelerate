from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field
import modify_query

class url_item(Item):
    url= Field()
    keywords = Field()
    title = Field()
    linksTo = Field()

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
            texts = response.xpath("//%s/text()" % (tag)).extract()
            for text in texts:
                text =  text.encode("ascii", "ignore")
                result = modify_query.query(text)
                item['keywords'] = item['keywords'] + result
        item['title'] = response.xpath("//title/text()").extract_first()
        item['keywords'] = set(item['keywords'])
        item['linksTo'] = []
        for link in LxmlLinkExtractor(allow=(self.allowed_domains),deny = ()).extract_links(response):
            item['linksTo'].append(link.url)
        return item
