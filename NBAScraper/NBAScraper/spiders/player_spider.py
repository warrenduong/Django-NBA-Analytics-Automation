
# importing the scrapy module
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from NBAScraper.NBAScraper.items import ScraperItem


class ExtractPlayer(scrapy.Spider):
    name = "extract"

    start_urls = [
        'https://www.basketball-reference.com/leagues/NBA_2021_totals.html', ]

    def parse(self, response):

        # define our scraper item
        item = ScraperItem()

        # body
        table = response.xpath('//*[@id="totals_stats"]/tbody')
        season = response.xpath(
            '//*[@id="meta"]/div[2]/h1/span[1]/text()').extract_first()

        # loop through all rows
        for row in table.xpath('.//tr'):

            item['season'] = season

            player = row.xpath('.//td/a/text()').extract_first()
            if player is None:
                continue
            else:
                item['player'] = player

            pos = row.xpath('.//td[2]/text()').extract_first()
            item['pos'] = pos

            age = row.xpath('.//td[3]/text()').extract_first()
            item['age'] = age

            tm = row.xpath('.//td[4]/a/text()').extract_first()
            if tm is not None:
                item['tm'] = tm
            else:
                tm = row.xpath('.//td[4]/text()').extract_first()
                item['tm'] = tm

            g = row.xpath('.//td[5]/text()').extract_first()
            item['g'] = g

            gs = row.xpath('.//td[6]/text()').extract_first()
            item['gs'] = gs

            mp = row.xpath('.//td[7]/text()').extract_first()
            item['mp'] = mp

            fg = row.xpath('.//td[8]/text()').extract_first()
            item['fg'] = fg

            fga = row.xpath('.//td[9]/text()').extract_first()
            item['fga'] = fga

            fg_pct = row.xpath('.//td[10]/text()').extract_first()
            item['fg_pct'] = fg_pct

            three_pt = row.xpath('.//td[11]/text()').extract_first()
            item['three_pt'] = three_pt

            three_pt_attempt = row.xpath('.//td[12]/text()').extract_first()
            item['three_pt_attempt'] = three_pt_attempt

            three_pt_pct = row.xpath('.//td[13]/text()').extract_first()
            item['three_pt_pct'] = three_pt_pct

            two_pt = row.xpath('.//td[14]/text()').extract_first()
            item['two_pt'] = two_pt

            two_pt_attempt = row.xpath('.//td[15]/text()').extract_first()
            item['two_pt_attempt'] = two_pt_attempt

            two_pt_pct = row.xpath('.//td[16]/text()').extract_first()
            item['two_pt_pct'] = two_pt_pct

            efg_pct = row.xpath('.//td[17]/text()').extract_first()
            item['efg_pct'] = efg_pct

            ft = row.xpath('.//td[18]/text()').extract_first()
            item['ft'] = ft

            fta = row.xpath('.//td[19]/text()').extract_first()
            item['fta'] = fta

            ft_pct = row.xpath('.//td[20]/text()').extract_first()
            item['ft_pct'] = ft_pct
            
            orb = row.xpath('.//td[21]/text()').extract_first()
            item['orb'] = orb
            
            drb = row.xpath('.//td[22]/text()').extract_first()
            item['drb'] = drb
            
            trb = row.xpath('.//td[23]/text()').extract_first()
            item['trb'] = trb
            
            ast = row.xpath('.//td[24]/text()').extract_first()
            item['ast'] = ast
            
            stl = row.xpath('.//td[25]/text()').extract_first()
            item['stl'] = stl
            
            blk = row.xpath('.//td[26]/text()').extract_first()
            item['blk'] = blk
            
            tov = row.xpath('.//td[27]/text()').extract_first()
            item['tov'] = tov
            
            pf = row.xpath('.//td[28]/text()').extract_first()
            item['pf'] = pf
            
            pts = row.xpath('.//td[29]/text()').extract_first()
            item['pts'] = pts
            

            yield item

        print(item)
