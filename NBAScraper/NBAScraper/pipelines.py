# Define your item pipelines here


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import psycopg2
from psycopg2 import connect
import os


class PostgresPipeline():
    def __init__(self):

        # Config details
        config = {
            "host": "localhost",
            "dbname": "NBA_Stats",
            "user": os.getenv("admin_user"),
            "password": os.getenv("db_password"),
            "port": "5432"
        }
        self.conn = psycopg2.connect(**config)

        # Create/Connect to database
        self.cur = self.conn.cursor()

        # Create cursor, used to execute commands
        self.conn.autocommit = True

        # Create table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS player_stats(
            key text,
            player text, 
            pos text,
            age integer,
            tm text,
            g integer,
            gs integer,
            mp integer,
            fg integer,
            fga integer,
            fg_pct float,
            three_pt integer,
            three_pt_attempt integer,
            three_pt_pct float,
            two_pt integer,
            two_pt_attempt integer,
            two_pt_pct float,
            efg_pct float,
            ft integer,
            fta integer,
            ft_pct float,
            orb integer,
            drb integer,
            trb integer,
            ast integer,
            stl integer,
            blk integer,
            tov integer,
            pf integer,
            pts integer
        )
        """)

    def process_item(self, item, spider):

        # Define insert statement
        self.cur.execute("""
            INSERT INTO player_stats 
            (key, player, pos, age, tm,
            g, gs, mp, fg, fga,
            fg_pct, three_pt, three_pt_attempt, three_pt_pct, two_pt,
            two_pt_attempt, two_pt_pct, efg_pct, ft, fta,
            ft_pct, orb, drb, trb, ast,
            stl, blk, tov, pf, pts, 
            season) 
            VALUES (%s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s)
        """,
                         (
                             item["player"] + ' ' + item["tm"],
                             item["player"],
                             item["pos"],
                             item["age"],
                             item["tm"],
                             item["g"],
                             item["gs"],
                             item["mp"],
                             item["fg"],
                             item["fga"],
                             item["fg_pct"],
                             item["three_pt"],
                             item["three_pt_attempt"],
                             item["three_pt_pct"],
                             item["two_pt"],
                             item["two_pt_attempt"],
                             item["two_pt_pct"],
                             item["efg_pct"],
                             item["ft"],
                             item["fta"],
                             item["ft_pct"],
                             item["orb"],
                             item["drb"],
                             item["trb"],
                             item["ast"],
                             item["stl"],
                             item["blk"],
                             item["tov"],
                             item["pf"],
                             item["pts"],
                             item['season']
                         ))

        # Execute insert of data into database
        self.conn.commit()
        return item


class NbaScraperPipeline:
    def process_item(self, item, spider):

        line = json.dumps(dict(item), ensure_ascii=False).encode(
            'utf-8').decode('latin1') + ",\n"
        self.file.write(line)

        return item

    def open_spider(self, spider):
        self.file = open('scraped_result.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()


