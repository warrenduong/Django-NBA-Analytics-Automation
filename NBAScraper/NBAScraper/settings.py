# Scrapy settings for NBAScraper project
BOT_NAME = 'NBAScraper'

SPIDER_MODULES = ['NBAScraper.NBAScraper.spiders']
NEWSPIDER_MODULE = 'NBAScraper.NBAScraper.spiders'

FEED_EXPORT_ENCODING: 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'NBAScraper.NBAScraper.pipelines.PostgresPipeline': 300,
    'NBAScraper.NBAScraper.pipelines.NbaScraperPipeline': 400,
}
