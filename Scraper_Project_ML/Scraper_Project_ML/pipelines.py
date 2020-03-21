# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from Scraper_Project_ML.settings import *


class ScraperProjectMlPipeline(object):

    # Pipeline To Store Data in MongoDB for Both the League Table and Competittion Table
    def __init__(self):
        self.client = MongoClient(DATABASE_IP_LEAGUE, DATABASE_PORT_LEAGUE)
        self.db = self.client[DATABASE_NAME_LEAGUE]
        self.league_collection = self.db[DATABASE_COLLECTION_LEAGUE]
        self.competition_collection = self.db[DATABASE_COMPETITION_LEAGUE]
        self.manager_collection = self.db[DATABASE_MANAGER]

    def process_item(self, item, spider):

        # print(f"item received from league pipeline is {item}")

        # For League Level Standing Data
        if item["collection_name"] == "League":
            print("League Table")
            self.league_collection.insert_one(dict(item))

        # For Competition Level Standing Data
        elif item["collection_name"] == "Competition":
            print("Competition Table")
            self.competition_collection.insert_one(dict(item))

        # For Manager Level Standing Data
        elif item["collection_name"] == "Manager":
            print("Manager Table")
            _ = dict(item)
            for key, value in _.items():
                if value == "-":
                    # print(key, value)
                    _[key] = "0"
                    # print(_)
            self.manager_collection.insert_one(_)
