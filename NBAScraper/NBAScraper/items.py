import scrapy
from scrapy_djangoitem import DjangoItem
from PlayersDashboard.models import PlayerStats
from scrapy import Field, Item


class ScraperItem(Item):

    key = Field()
    player = Field()
    pos = Field()
    age = Field()
    tm = Field()
    g = Field()
    gs = Field()
    mp = Field()
    fg = Field()
    fga = Field()
    fg_pct = Field()
    three_pt = Field()
    three_pt_attempt = Field()
    three_pt_pct = Field()
    two_pt = Field()
    two_pt_attempt = Field()
    two_pt_pct = Field()
    efg_pct = Field()
    ft = Field()
    fta = Field()
    ft_pct = Field()
    orb = Field()
    drb = Field()
    trb = Field()
    ast = Field()
    stl = Field()
    blk = Field()
    tov = Field()
    pf = Field()
    pts = Field()
    season = Field()
