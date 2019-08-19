# 因为课程指引的URL只能带去电影列表，而电影列表并没有地区，类型 这两个字段（要进去电影详情页才有）所以改用Top250这个页面来完成要求。
import json
import pandas as pd
import os
import time
import requests
import unicodedata
import random
from lxml import etree
from fake_useragent import UserAgent

# 电影类
class Movie(object):
    def __init__(self, name, year, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link
        self.year = year

class MovieCrawler(object):
    def __init__(self):
        # init URL
        self.init_url = "https://movie.douban.com/top250"
        # movies list
        self.movies = []

    # crawl movies in website
    def crawl_movies(self, start = 0):
        # used to create fake user agent
        ua = UserAgent()
        # request header
        headers = {"UserAgent":ua.random, "Connection":"keep-alive"}
        # request params
        params = {"start":start, "filter":""}
        # send request
        response = requests.get(self.init_url, params = params, headers = headers)
        # use xml to parse content
        tree = etree.HTML(response.text)
        items = tree.xpath("//div[@class='article']//li")
        for item in items :
            info_link = "".join(item.xpath(".//div[@class='hd']/a/@href"))
            cover_link = "".join(item.xpath(".//div[@class='pic']/a/img/@src"))
            name = "".join(item.xpath(".//div[@class='pic']/a/img/@alt"))
            p = "".join(item.xpath(".//div[@class='bd']/p/text()")).strip()
            # cause p content include \xa0, so use normalize to deal with the situation
            p = unicodedata.normalize("NFKD",p)
            # split category and location from directors
            cl_lst = p.split("\n")[1].strip().split("/")
            # parse year
            year = cl_lst[0].strip() if cl_lst else ""
            # parse location
            location = list(filter(None, cl_lst[1].split(" ")))[0].strip() if len(cl_lst) > 1 else ""
            categories = list(filter(None, cl_lst[2].split(" ")))  if len(cl_lst) > 2 else ""
            # cause "Plot" type always in first element after split category field,
            # so i chose category with random index which inside 2 or more categories.
            category = ""
            if categories:
                random_category_index = random.randint(0, len(categories) - 1)
                category = categories[random_category_index]
            rate = "".join(item.xpath(".//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()"))
    
            # build Movie object
            movie = Movie(name, year, rate, location, category, info_link, cover_link)
            # save object in movie list by using object__dict__ 
            self.movies.append(movie.__dict__)
        # next page flag, if this flag carry content, then calling this method again
        has_next = tree.xpath("//span[@class='next']/link[@rel='next']/@href")
        # sleep random 2-5 seconds
        time.sleep(random.randint(2,5))
        if has_next:
           start += 25
           self.crawl_movies(start = start)
        else:
           self.save_csv()

    # Serialization from object to csv file
    def save_csv(self):
        df = pd.DataFrame(self.movies)
        df.to_csv("./movie.csv",index=False)
    
    def analysis_csv(self):
        df_movie = pd.read_csv("./movie.csv")
        # remove NONE Chinese character
        df_movie["category"] = df_movie["category"].str.replace("[^\u4e00-\u9fa5]", "")
        df_movie["location"] = df_movie["location"].str.replace("[^\u4e00-\u9fa5]", "")
        # remove NONE digital character
        df_movie["year"] = df_movie["year"].str.replace("\D", "")
        
        # grouping by category and location , then calc size
        gby_df = df_movie.groupby(by = ['category', 'location'], as_index = False).size()
        # add oc_time as new column's name and sort value by category first then oc_time
        sorted_gby_df = gby_df.reset_index(name = "oc_time").sort_values(by = ["category", "oc_time"],ascending = False)
        # calc each oc_time percent
        sorted_gby_df["percent"] = sorted_gby_df.groupby("category")["oc_time"].apply(lambda x : x / x.sum())
        # take 3 top level rows from each category group
        top_items = sorted_gby_df.groupby("category").head(3)
        # write to file
        self.write_analysis_result(top_items)
    
    # write result to output.txt
    def write_analysis_result(self, top_items):
        # open output.txt with 'w+' mode
        f = open("./output.txt", "w+")
        for index ,item in top_items.iterrows():
            # format float to %
            percent = "{:.2f}".format(item["percent"] * 100)
            # build output sentence
            row = f"{item['location']} 占领了 {percent}% 的 {item['category']}类型电影 \n" 
            # write output to file
            f.write(row)
        f.close()



mc = MovieCrawler()
# mc.analysis_csv()
# mc.crawl_movies()

