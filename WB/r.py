import requests
from bs4 import BeautifulSoup as BS
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("wb")


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.111YaBrowser / 21.2.1.107Yowser / 2.5Safari / 537.36",
            "Accept-Language": "ru"
        }

    def load_page(self, page: int = None):
        url = "https://www.wildberries.kg/catalog/0/search.aspx?search=%D1%85%D1%83%D0%B4%D0%B8&xsearch=true"
        response = self.session.get(url)
        response.raise_for_status()
        return response.text

    def parse_page(self, text: str):
        soup = BS(text, "lxml")
        container = soup.select("div.dtList.i-dtList.j-card-item")
        for block in container:
            self.parse_block(block)

    def parse_block(self, block):
        # logger.info(block)
        # logger.info("="*100)
        name = block.select_one("div.dtlist-inner-brand-name")
        brand_name = name.select_one("strong.brand-name.c-text-sm").text
        brand_name = brand_name.replace("/", "").strip()
        url_block = block.select_one('a.ref_goods_n_p.j-open-full-product-card')
        name = name.select_one("span.goods-name.c-text-sm").text
        url = "https://www.wildberries.kg"+url_block.get("href")
        link = url_block.select_one("div.l_class")
        link1 = link.select_one("img.thumbnail").get("data-original")
        if link1 is None:
            link1 = link.select_one("img.thumbnail").get("src")
        else:
            pass
        link = f"http:{link1}"

        logger.info("%s, %s %s, %s", url, brand_name, name, link)

    def run(self):
        text = self.load_page()
        self.parse_page(text)


parse = Client()
parse.run()