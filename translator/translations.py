from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

headers = {'User-Agent': 'Chrome/103.0.0.0'}


# Static


def static_search(url):
    static_results = []
    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    for i in soup.find_all("span", attrs={"class": "display-term"}):
        static_results.append(i.text)
    return static_results

# Dynamic


def dynamic_search(url):
    dynamic_results = []
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.minimize_window()
    driver.get(url)
    time.sleep(2)
    r = driver.page_source
    soup = BeautifulSoup(r,'html.parser')
    results = []
    filter_html = soup.find('div', attrs = {'id':'mt-box'}).find('div', attrs = {'class': 'trg ltr'}).find('div', attrs = {'class': None})
    translation = filter_html.find('span', attrs = {"class": 'text'}).text
    dynamic_results.append(translation)
    return dynamic_results


def translation_result(url):
    result = static_search(url)
    if len(result) != 0:
        return result
    else:
        return dynamic_search(url)

