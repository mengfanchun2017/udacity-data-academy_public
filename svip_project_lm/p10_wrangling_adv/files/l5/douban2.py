#!/usr/bin/env python
#-*-coding:utf-8 -*-
import requests
from lxml import etree
from pyquery import PyQuery
import re
import numpy as np
from time import sleep
import json

# 设定搜集网页,此网页为 top250 的网页,包括了需要的数据
# 如果是从单独页面来抓取,需要使用ip池,否则会反扒
INITIAL_URL = "https://movie.douban.com/top250"

HEADERS = {
    "User-Agent":"", # 添加 user-agent
    "Connection": "keep-alive",
    "Host": "movie.douban.com"
}

COLUMNS = [
    "url", "title", "rank", "directors", "writers", "actors", "categories", 
    "product_country", "language", "release_date", "duration", "another_name", 
    "imdb"
]

# TODO: 获取每个页面
def get_web(url):
    web = requests.request("GET", url, headers=HEADERS)
    query = PyQuery(web.text)
    next_url = query("span.next").children("a").attr("href")
    return query, next_url

# TODO: 获取 top250 的每个页面中电影条目 URL
def get_artile(content):
    articles = content("div.info")
    for item in articles.items():
        article = item("a").attr("href")
        yield article

# TODO: 检查并获取需要的数据
def check(tree, target):
    for item in tree.cssselect("div#info > span"):
        if item.text and target in item.text:
            return item.xpath("./following-sibling::text()")[0].strip()
    else:
        return np.nan

# TODO: 从每个页面中去获取需要的电影信息
def article_info(url):
    web = requests.request("GET", url, headers=HEADERS, timeout=100)
    
    if web.status_code == requests.codes.OK:
        query = PyQuery(web.text)
        rank = query(".top250-no").text()
        title = query("h1").text()

        # 得到 div#info 元素，筛选出需要要的资源元素
        content = query("div#info")
        directors = content("span:first-child a").text()
        writers = content("span:nth-child(3)").text().replace(r"编剧:", "").strip()
        actors = content("span:nth-child(5)").text().replace(r"主演:", "").strip()
        
        # 其他不方便使用 pyquery 来筛选的数据使用 etree 中的 xpath 的方式来筛选
        tree = etree.HTML(web.text, etree.HTMLParser())
        categories = r"/".join(tree.xpath("//span[@property='v:genre']/text()")) # 类型
        release_date = r"/".join(tree.xpath("//span[@property='v:initialReleaseDate']/text()")) # 发型日期
        duration = tree.xpath("//span[@property='v:runtime']/text()")[0] # 时长

        another_name = check(tree, "又名") # 别名
        product_country = check(tree, "制片国家/地区") # 制片国家
        language = check(tree, "语言") # 语言
        # product_country = tree.xpath("//div[@id='info']/span[7]")[-1].xpath("./following-sibling::text()")[0].strip() # 制片国家
        # language = tree.xpath("//div[@id='info']/span[8]")[-1].xpath("./following-sibling::text()")[0].strip() # 语言
        # another_name = tree.xpath("//div[@id='info']/span[14]")[-1].xpath("./following-sibling::text()")[0].strip() # 别名
        try:
            imdb = tree.cssselect("div#info > span:last-of-type + a:first-of-type")[-1].attrib["href"]
        except:
            imdb = tree.cssselect("div#info > span.pl + a[rel='nofollow']:first-of-type")[-1].attrib["href"]

        data = dict(
            url=url,
            title=title,
            rank=rank,
            directors=directors,
            writers=writers,
            actors=actors,
            categories=categories,
            product_country=product_country,
            language=language,
            release_date=release_date,
            duration=duration,
            another_name=another_name,
            imdb=imdb
        )
        return data



if __name__ == "__main__":
    unread = []
    # TODO: 获取初始页面信息
    text, next_url = get_web(INITIAL_URL)
    # TODO: 解析初始页面信息
    for url in get_artile(text):
        with open("douban.json", "a", encoding="utf-8") as file:
            try:
                print(url)
                sleep(3)
                data = article_info(url)
                file.write(json.dumps(data, ensure_ascii=False) + "\n")
            except requests.RequestException:
                print("No information: ", url)
                unread.append(url)
                continue
        
    # TODO: 处理后续页面信息
    while next_url:
        url = INITIAL_URL + next_url
        text, next_url = get_web(url)
        for url in get_artile(text):
            with open("douban.json", "a", encoding="utf-8") as file:
                try:
                    print(url)
                    sleep(1)
                    data = article_info(url)
                    file.write(json.dumps(data, ensure_ascii=False) + "\n")
                except requests.RequestException:
                    print("No information: ", url)
                    continue