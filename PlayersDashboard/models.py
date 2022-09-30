from django.db import models


# Create your models here.
class PlayerStats(models.Model):
    __tablename__ = "player_stats"
    key = models.TextField(db_column='key', primary_key=True, blank=True)
    player = models.TextField(db_column='player')
    pos = models.TextField(db_column='pos', blank=True, null=True)
    age = models.IntegerField(db_column='age', blank=True, null=True)
    tm = models.TextField(db_column='tm', blank=True, null=True)
    g = models.IntegerField(db_column='g', blank=True, null=True)
    gs = models.IntegerField(db_column='gs', blank=True, null=True)
    mp = models.IntegerField(db_column='mp', blank=True, null=True)
    fg = models.IntegerField(db_column='fg', blank=True, null=True)
    fga = models.IntegerField(db_column='fga', blank=True, null=True)
    fg_pct = models.FloatField(db_column='fg_pct', blank=True, null=True)
    three_pt = models.IntegerField(db_column='three_pt', blank=True, null=True)
    three_pt_attempt = models.IntegerField(
        db_column='three_pt_attempt', blank=True, null=True)
    three_pt_pct = models.FloatField(
        db_column='three_pt_pct', blank=True, null=True)
    two_pt = models.IntegerField(db_column='two_pt', blank=True, null=True)
    two_pt_attempt = models.IntegerField(
        db_column='two_pt_attempt', blank=True, null=True)
    two_pt_pct = models.FloatField(
        db_column='two_pt_pct', blank=True, null=True)
    efg_pct = models.FloatField(db_column='efg_pct', blank=True, null=True)
    ft = models.IntegerField(db_column='ft', blank=True, null=True)
    fta = models.IntegerField(db_column='fta', blank=True, null=True)
    ft_pct = models.FloatField(db_column='ft_pct', blank=True, null=True)
    orb = models.IntegerField(db_column='orb', blank=True, null=True)
    drb = models.IntegerField(db_column='drb', blank=True, null=True)
    trb = models.IntegerField(db_column='trb', blank=True, null=True)
    ast = models.IntegerField(db_column='ast', blank=True, null=True)
    stl = models.IntegerField(db_column='stl', blank=True, null=True)
    blk = models.IntegerField(db_column='blk', blank=True, null=True)
    tov = models.IntegerField(db_column='tov', blank=True, null=True)
    pf = models.IntegerField(db_column='pf', blank=True, null=True)
    pts = models.IntegerField(db_column='pts', blank=True, null=True)
    season = models.TextField(db_column='season', blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'player_stats'
