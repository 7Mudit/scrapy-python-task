import scrapy

class ArtistBioSpider(scrapy.Spider):
    name = 'artist_bio' 
    allowed_domains = ['localhost']  # Replace with the actual domain
    start_urls = ['http://127.0.0.1:5500/index.html']  # Replace with the artist's page

    def parse(self, response):
     bio = response.css('div.big-artist-list-bio p::text').get()
     yield {'artist_bio': bio}
    
    