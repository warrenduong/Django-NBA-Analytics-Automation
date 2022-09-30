from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from NBAScraper.NBAScraper import settings as my_settings
from NBAScraper.NBAScraper.spiders.player_spider import ExtractPlayer


class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(ExtractPlayer)
        process.start()
