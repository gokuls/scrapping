import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from datascience.items import DatascienceItem



class DatascienceCrawlerSpider(CrawlSpider):
    name = 'datascience_crawler'
    allowed_domains = ['datascience.stackexchange.com']
    start_urls = ['https://datascience.stackexchange.com/questions']

    rules = (
        Rule(LinkExtractor(allow=r'questions\?tab=newest&page=[0-9]', restrict_xpaths=('//a[@rel="next"]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = DatascienceItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
