from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

service = webdriver.EdgeService(executable_path="C:/Users/gaura/OneDrive/Desktop/python/P128/msedgedriver.exe")
browser = webdriver.Edge(service= service)
browser.get(START_URL)

time.sleep(10)

scarped_data = []

def scrape():

    soup = BeautifulSoup(browser.part_source, "html.parser")

    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    table_body = bright_star_table.find('tbody')

    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')

        temp_list = []

        for col_data in table_cols:

            data = col_data.text.strip()

            temp_list.append(data)
        
        scarped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0,len(scarped_data)):

    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)

headers = ['Star_names, Distance, Mass, Radius, Lum']

star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")

