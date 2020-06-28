# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pandas as pd

class MaoyanmoviesPipeline:
    def process_item(self, item, spider):
        # return item
        df = pd.DataFrame(dict(item), index=[0])
        if os.path.exists('./maoyanmovies_scrapy_result.csv'):
            header = False
        else:
            header = True
        df.to_csv('./maoyanmovies_scrapy_result.csv', mode='a', index=False, header=header)
        return item
