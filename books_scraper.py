import scrapy
class bookspider(scrapy.Spider):
    name = 'booksspider'
    start_urls = ["https://books.toscrape.com"]

    def parse(self,response):
        for article in response.css ('article.product.pod'):
            yield{
                'price': article.css(".price_color::text").extract_first(),
                'title': article.ss("h3>a::atttr(title)").extract_first()
            }
            next = response.css('.next>a::ttr(href)').extract_first()
            if next:
                yield response.follow(next,self.parse)
