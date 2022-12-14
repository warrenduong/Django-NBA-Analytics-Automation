# Generated by Django 4.1.1 on 2022-09-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlayerStats",
            fields=[
                (
                    "key",
                    models.TextField(
                        blank=True, db_column="key", primary_key=True, serialize=False
                    ),
                ),
                ("player", models.TextField(db_column="player")),
                ("pos", models.TextField(blank=True, db_column="pos", null=True)),
                ("age", models.IntegerField(blank=True, db_column="age", null=True)),
                ("tm", models.TextField(blank=True, db_column="tm", null=True)),
                ("g", models.IntegerField(blank=True, db_column="g", null=True)),
                ("gs", models.IntegerField(blank=True, db_column="gs", null=True)),
                ("mp", models.IntegerField(blank=True, db_column="mp", null=True)),
                ("fg", models.IntegerField(blank=True, db_column="fg", null=True)),
                ("fga", models.IntegerField(blank=True, db_column="fga", null=True)),
                (
                    "fg_pct",
                    models.FloatField(blank=True, db_column="fg_pct", null=True),
                ),
                (
                    "three_pt",
                    models.IntegerField(blank=True, db_column="three_pt", null=True),
                ),
                (
                    "three_pt_attempt",
                    models.IntegerField(
                        blank=True, db_column="three_pt_attempt", null=True
                    ),
                ),
                (
                    "three_pt_pct",
                    models.FloatField(blank=True, db_column="three_pt_pct", null=True),
                ),
                (
                    "two_pt",
                    models.IntegerField(blank=True, db_column="two_pt", null=True),
                ),
                (
                    "two_pt_attempt",
                    models.IntegerField(
                        blank=True, db_column="two_pt_attempt", null=True
                    ),
                ),
                (
                    "two_pt_pct",
                    models.FloatField(blank=True, db_column="two_pt_pct", null=True),
                ),
                (
                    "efg_pct",
                    models.FloatField(blank=True, db_column="efg_pct", null=True),
                ),
                ("ft", models.IntegerField(blank=True, db_column="ft", null=True)),
                ("fta", models.IntegerField(blank=True, db_column="fta", null=True)),
                (
                    "ft_pct",
                    models.FloatField(blank=True, db_column="ft_pct", null=True),
                ),
                ("orb", models.IntegerField(blank=True, db_column="orb", null=True)),
                ("drb", models.IntegerField(blank=True, db_column="drb", null=True)),
                ("trb", models.IntegerField(blank=True, db_column="trb", null=True)),
                ("ast", models.IntegerField(blank=True, db_column="ast", null=True)),
                ("stl", models.IntegerField(blank=True, db_column="stl", null=True)),
                ("blk", models.IntegerField(blank=True, db_column="blk", null=True)),
                ("tov", models.IntegerField(blank=True, db_column="tov", null=True)),
                ("pf", models.IntegerField(blank=True, db_column="pf", null=True)),
                ("pts", models.IntegerField(blank=True, db_column="pts", null=True)),
                ("season", models.TextField(blank=True, db_column="season", null=True)),
            ],
            options={"db_table": "player_stats", "managed": True,},
        ),
    ]
