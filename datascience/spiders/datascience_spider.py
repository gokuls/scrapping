from scrapy import Spider
from scrapy.selector import Selector

from datascience.items import DatascienceItem


class datascience_spider(Spider):
    name = "datascience"
    allowed_domains = ["datascience.stackexchange.com"]
    start_urls = [
        "https://datascience.stackexchange.com/questions",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = DatascienceItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item