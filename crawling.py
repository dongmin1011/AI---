import warnings 
warnings.filterwarnings('ignore') 
import requests
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
for i in range(1, 11):
    driver.get(f'https://m.koita.or.kr/m/mobile/mem_knowledge/ktip_list.aspx?page={i}&')


    strong_elements = driver.find_elements(By.TAG_NAME, "strong")
    for strong_element in strong_elements:
        text = strong_element.text
        print(text)
# titles=[]
# for content in contents:
#     titles.append(content.find_element(By.CSS_SELECTOR, selector).text)
# print(len(titles), titles[:3])

# url = 'https://m.koita.or.kr/m/mobile/mem_knowledge/ktip_list.aspx?page=1&'

# # response
# headers={
#     # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
#     # 'Referer':'https://techblog.woowahan.com/',
#     # 'Cookie':'_ga=GA1.1.1096902407.1698486779; _ga_JQ34XQDGNB=GS1.1.1698486779.1.1.1698487089.0.0.0',
#     # 'Sec-Ch-Ua-Platform':"Windows",
#     # 'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#     # 'Origin':'https://techblog.woowahan.com',
#     # 'X-Requested-With':'XMLHttpRequest',
#     # 'Sec-Fetch-Site':'same-origin',
#     # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
# }
# response = requests.get(url, headers=headers)
# response
