from nltk.corpus.reader.chasen import test
from TextRank import TextRank
from bs4 import BeautifulSoup
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import requests
import re
import networkx as nx

url = "https://www.imdb.com/chart/top/"

#make beautifulsoup object
def r_soup(web_url):
    page = requests.get(web_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# print(soup.prettify())    


def link_extractor():
    results = r_soup(url).find_all("td", class_="titleColumn")
    links = []
    new_url = re.sub("/chart/top/","",url)
    for result in results:
        link = result.find("a").attrs.get('href')
        complete_link =  new_url + link
        links.append(complete_link)
    return links

# print(links) 

def story_line(web_url):
    movie_story=[]
    for url in web_url:
        sub_page = r_soup(url)
        # story_line_txt =sub_page.find("div",id="titleStoryLine").find("div",class_=("inline canwrap")).find("span").text
        story_line_txt = sub_page.find("div", class_ = "Storyline__StorylineWrapper-sc-1b58ttw-0").find("div", class_ = "ipc-overflowText").find("div", class_ = "ipc-html-content").find("div").text
        # title= re.sub(r"[(\d)]","",sub_page.find("div",class_="title_wrapper").find("h1").text)
        t = re.sub(r"[(\d)]", "", sub_page.find("div", class_ = "TitleBlock__TitleContainer-sc-1nlhx7j-1").find("h1").text)
        movie_story.append(dict(title = re.sub("[\...]$","",t), stry=story_line_txt))
    # print(movie_story)
    return movie_story

