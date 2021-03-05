import requests
from bs4 import BeautifulSoup as BS
import logging
import asyncio
import aiohttp

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("wb")


class Article:

    def __init__(self):
        self.url = "https://24.kg/"
        self.page = None
        self.articles_info = []
        self.articles_link = []

    def get_requests(self):
        response = requests.get(url=self.url)
        soup = BS(response.content, "lxml")

        if response.status_code == 200:
            return soup
        else:
            logger.info("Ошибка связанная с доступом в сайт")

    def get_page(self):
        html = self.get_requests()
        resp_text = html.select("div.one")
        for i, x in zip(resp_text, resp_text):
            i = i.text.replace("\xa0", " ")
            self.articles_info.append(i.strip())
            x = "https://24.kg" + x.select_one("a").get("href")
            self.articles_link.append(x)
        # print(len(self.articles_link))
        # print(len(self.articles_info))
        print(self.articles_link)
        return self.articles_info, self.articles_link


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


async def main(url):
    t = []
    html = await fetch(url)
    soup = BS(html, "lxml")
    text = soup.select_one("h1.newsTitle")
    t.append(text)
    return t


async def run(urls):
    return await asyncio.gather(*[main(url) for url in urls])


a = Article()
urls = a.get_page()[1][:20]
loop = asyncio.get_event_loop()
print(loop.run_until_complete(run(urls)))
