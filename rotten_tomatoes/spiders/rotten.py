import scrapy

class RottenSpider(scrapy.Spider):
    name = "rotten"
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/"]

    def parse(self, response):
        title = response.xpath('//*[@id="media-lists"]/div[4]/div/div[2]/div/section/text-list/h2/text()').getall()
        for i in range(1, len(title)+1):
            for _ in range(1, 11):
                movies = response.xpath(f'//*[@id="media-lists"]/div[4]/div/div[2]/div[{i}]/section/text-list/ul/li[{_}]/a/span/text()').getall()


                top_tens = {
                        "category": title[i-1],
                        "movie": movies[0],
                        "rating": movies[1].strip(),
                    }

                info = response.xpath(f'////*[@id="media-lists"]/div[4]/div/div[2]/div[{i}]/section/text-list/ul/li[{_}]/a[2]/@href').get()
                if info is not None:
                    yield response.follow(info, callback=self.description, meta = {"top_tens": top_tens})

                # return self.logger.info(f"Got successful response from {response.url}")
    def description(self, response):
        data = response.meta['top_tens']
        movie_info = response.xpath('//*[@id="movie-info"]/div/div/drawer-more/p/text()').get()
        if movie_info is None:
            movie_info = response.xpath('//*[@id="episodes"]/div/ul/li[1]/div/drawer-more/p/text()').get()
        if movie_info is not None:
            movie_info = movie_info.strip()
        data['description'] = movie_info
        yield data

"""most_popular_name = response.xpath('//section[@class="dynamic-text-list "]/text-list/ul[@slot="list-items"]/li/a/span/text()').getall()
movie_categories = response.xpath('//section[@class="dynamic-text-list "]/text-list/h2/text()').getall()
['Popular Streaming Movies', 'Most Popular TV on RT ', 'New TV This Week']
for categories in response.xpath('//section[@class="dynamic-text-list "]'):
yield {
"categories": categories.xpath('//text-list/h2/text()').getall()
}
"""