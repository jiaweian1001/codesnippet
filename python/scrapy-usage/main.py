"""
This is a scrapy usage demo. It can be run by:
    scrapy runspider main.py
Or if you want to save the output to a file:
    scrapy runspider main.py -o output.json
"""
import scrapy

class ImageSpider(scrapy.Spider):
    """
    This is a spider for crawling images from a website.
    """
    name = 'image_spider'
    allowed_domains = 'www.example.com'
    start_urls = ['http://www.example.com']

    def parse(self, response, **kwargs):
        # Get all links from the page
        links = response.css('a::attr(href)').getall()
        for link in links:
            # Filter out links that are not from the same domain
            if self.allowed_domains in link:
                print("follow link:"+link)
                yield scrapy.Request(link, callback=self.parse)
        # Get all image links from the page
        image_links = response.css('img::attr(src)').getall() + response.css('img::attr(data-src)').getall()
        for image_link in image_links:
            if image_link.startswith("http"):
                yield {"image_link": image_link}