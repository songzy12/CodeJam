import logging
from typing import Generator

from scrapy import Spider, Request
from scrapy.http.response import Response
from scrapy_playwright.page import PageMethod


class KickstartSpider(Spider):

    name = "kickstart"
    custom_settings = {
        "TWISTED_REACTOR":
        "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "https":
            "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler"
        },
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "proxy": {
                "server": "http://localhost:10809"
            },
            "headless": False
        },
        # TODO: understand why the spider will not run with scrapy's header.
        "PLAYWRIGHT_PROCESS_REQUEST_HEADERS": None
    }

    start_urls = [
        "https://codingcompetitions.withgoogle.com/kickstart/archive/2013"
    ]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        logging.getLogger("scrapy.core.engine").setLevel(logging.WARNING)
        logging.getLogger("scrapy.core.scraper").setLevel(logging.WARNING)

    def start_requests(self):
        for start_url in self.start_urls:
            yield Request(
                url=start_url,
                meta={
                    "playwright":
                    True,
                    "playwright_page_methods": [
                        PageMethod(
                            "wait_for_selector",
                            '//div[@class="schedule-row schedule-row__past"]'),
                    ],
                },
            )

    def parse(self, response: Response) -> Generator:
        for round in response.xpath(
                '//div[@class="schedule-row schedule-row__past"]'):
            round_name = round.xpath(".//span/text()").get()
            round_link = round.xpath(".//a//@href").get()
            yield {round_name: round_link}
