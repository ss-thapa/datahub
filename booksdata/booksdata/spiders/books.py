import scrapy
from pathlib import Path
import pandas as pd

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f"books-{page}.html"
        Path(filename).write_bytes(response.body)


        df_data = []

        
        # save the content as files
        # path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        cards = response.css(".product_pod")
        for card in cards:
            title = card.css("h3>a::text").get()
            rating = card.css(".star-rating").attrib['class'].split(" ")[1]
            # print(rating)
            # print(title)
            image = card.css(".image_container img")
            # print(image)
            price =card.css(".price_color::text").get().replace('£', '')
            
            availability = card.css(".availability")
            
            instock = len(availability.css(".icon-ok")) > 0
            
            # if len(availability.css(".icon-ok")) > 0:
            #     inStock = True
            # else:
            #     inStock=False

            df_data.append({'title': title, 'rating':rating, 'price':price, 'instock':instock})
        
        df = pd.DataFrame(df_data)

        df.to_csv(f'books_data_{page}.csv', index=False)

        self.log(f'Saved file {'mybook'}')
            



            







