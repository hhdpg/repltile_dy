import scrapy
class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed = ["dmoz.org"]
    start_url = [
        "http://www.dmoz.org/Computers/Prpgramming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Prpgramming/Languages/Python/Resources/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename,"wb") as f :
            f.write(response.body)