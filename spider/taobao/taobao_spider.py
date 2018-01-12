import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB_TAOBAO]
driver = webdriver.Chrome("D:/mylibs/chromedriver/chromedriver.exe")
wait = WebDriverWait(driver, 10)


def search(keyword="美食"):
    driver.get("http://www.taobao.com")
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys(keyword)
        submit.click()

        total_pages = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text
        total_pages = re.search('(\d+)', total_pages).group(1)

        return int(total_pages)
    except TimeoutException as e:
        print('search timeout')


def next_page(page_number):
    try:
        inputbox = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        inputbox.clear()
        inputbox.send_keys(page_number)
        button.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
    except TimeoutException:
        next_page(page_number)
        print('next_page timeout')


def parse_page():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select('#mainsrp-itemlist .items .item')
    for item in items:
        product = {
            'image': item.select('.J_ItemPic')[0].attrs['data-src'],
            'url': item.select('.pic-link')[0].attrs['data-href'],
            'name': item.select('.title')[0].get_text().strip(),
            'price': item.select('.g_price-highlight > strong')[0].get_text(),
            'deal': item.select('.deal-cnt')[0].get_text(),
            'shop': item.select('.shop')[0].get_text().strip(),
            'location': item.select('.location')[0].get_text()
        }
        save_to_mongo(product)
        # print(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE_TAOBAO].insert(result):
            print('insert ok')
    except Exception as e:
        print(e)


def main():
    total = search()
    parse_page()
    for i in range(2, total + 1):
        # import time
        # time.sleep(2)
        next_page(i)
        parse_page()


if __name__ == '__main__':
    main()
    driver.close()
