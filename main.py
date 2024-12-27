from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top")

moviesList = driver.find_element(by=By.CSS_SELECTOR, value="ul.ipc-metadata-list.ipc-metadata-list--dividers-between.sc-a1e81754-0.iyTDQy.compact-list-view.ipc-metadata-list--base")

movies = moviesList.find_elements(By.TAG_NAME, value='li')

data = []

for movie in movies:
    posName = movie.find_element(By.TAG_NAME, value='h3').text
    rate = movie.find_element(By.CSS_SELECTOR, value='.ipc-rating-star--rating').text

    pos = posName.split('. ')[0]
    name = posName.split('. ')[1]

    data.append({
        'position': pos,
        'name': name,
        'rate': rate,
    })

df = pd.DataFrame(data)

df.to_excel(f"Top250Movies.xlsx", index=False)