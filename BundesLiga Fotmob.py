#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.fotmob.com/en-GB/leagues/54/stats/season/17801/players/rating"
driver = webdriver.Chrome("/path/to/chromedriver")
driver.get(url)
table_present = EC.presence_of_element_located((By.CLASS_NAME, "player-stats-table"))
WebDriverWait(driver, 10).until(table_present)
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height


table = driver.find_element(By.CLASS_NAME, "player-stats-table")


headers = [th.text.strip() for th in table.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "th")]


data_rows = []
for tr in table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
    data_row = [td.text.strip() for td in tr.find_elements(By.TAG_NAME, "td")]
    data_rows.append(data_row)


df = pd.DataFrame(data_rows, columns=headers)


excel_filename = "fotmob_data.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data scraped and saved to {excel_filename}")

driver.quit()

