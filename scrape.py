import bs4
import requests
import argparse
import sys
import os
import pandas as pd

parser = argparse.ArgumentParser(
    prog='python scrape.py', description='Scrape Bangla song lyrics from https://banglasonglyrics.com/')
parser.add_argument('filename', help='Filename for the csv file')
parser.add_argument('--start', type=int,
                    help='Select a starting page (default 0)')
parser.add_argument('--end', type=int,
                    help='Select an ending page (default 281)')
parser.add_argument('--verbose', type=int,
                    help='0 = False, 1 = True (default 1)')
args = parser.parse_args()

start, end, filename = args.start, args.end, args.filename
start = 1 if args.start == None else args.start
end = 281 if args.end == None else args.end
verbose = 1 if args.verbose == None else args.verbose
base_url = "https://banglasonglyrics.com/page/"


def scrape_single_article(article):
    try:
        title = article.find("h2", {"class": "entry-title"}).a.text
        category = article.find("span", {"class": "cat-links"}).a.text
        lyrics = article.find("div", {"class": "entry-content"}).text.strip()

        if(len(lyrics.split('\n')) < 2):
            return -1

        article_dict = {
            "title": title,
            "category": category,
            "lyrics": lyrics
        }

        return article_dict

    except:
        return -1


def scrape_a_page(id):
    write_counter = 0
    url = base_url + str(id)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content, features="html5lib")
    all_articles = soup.find_all("article", {"class": "post"})
    articles = []
    for article in all_articles:
        article_dict = scrape_single_article(article)
        if article_dict != -1:
            articles.append(article_dict)
            write_counter = write_counter + 1
    dataframe = pd.DataFrame(articles)
    dataframe.to_csv(filename, index=False,
                     mode="a", header=(id == start))
    return write_counter


counter = 0

for id in range(start, end+1):
    write_counter = scrape_a_page(id)
    counter += write_counter
    if verbose > 0:
        print(f"Page {id}/{end} is written to file")

print(
    f"All Done!\n{counter} lyrics from {end + 1 - start} pages were scraped!")
