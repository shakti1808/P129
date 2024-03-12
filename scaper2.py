from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

service = webdriver.EdgeService(executable_path="C:/Users/gaura/OneDrive/Desktop/python/P128/msedgedriver.exe")
browser = webdriver.Edge(service= service)
browser.get(START_URL)

time.sleep(10)

new_scarped_data = []

def scrape_more_data(hyperlink):

    try:
        page = requests.get(hyperlink)
     
        soup = BeautifulSoup(page.content, "html.parser")

        temp_list = []


        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
         
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
                   
        new_scarped_data.append(temp_list)


    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

scraped_df_1 = pd.read_csv("scraped_data.csv")

for index, row in scraped_df_1.iterrows():

    print(row['hyperlink'])
    scrape_more_data(row['hyperlink'])

    print(f"Data Scraping at hyperlink {index+1} completed")

print(new_scarped_data)

scraped_data = []

for row in new_scarped_data:
    replaced = []

    for el in row:
        el = el.replace("\n", "")
        replaced.append(el)


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["brown_dwarf","constellation", "right_ascension", "declination", "app._mag.", "distance", "spectral_type", "mass", "radius", "discovery_year"]

new_planet_df_1 = pd.DataFrame(scraped_data,columns = headers)

new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
