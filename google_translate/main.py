from encodings import utf_8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd

xls = pd.ExcelFile(r"New Sentences.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Banglish'].astype('string')


website_1 = "https://www.google.com/search?ie=UTF-8&q=google%20translator"

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(website_1)

language = driver.find_element(By.XPATH, '//span[@class="source-language"]')
language.click()

time.sleep(2)
bangla = driver.find_element(
    By.XPATH, '//input[@id="sl_list-search-box"]')
bangla.send_keys("bangla" + Keys.ENTER)


input_text = driver.find_element(
    By.XPATH, '//textarea[@id="tw-source-text-ta"]')
time.sleep(1)
out_csv = []
output_csv_file = "output_xl_new_sentences.csv"

# for i in range(len(var1)):
for i in range(len(var1)):
    out_csv = []
    # print(i)
    try:
        input_text.clear()
        input_text.send_keys(var1[i])

        # output_text = driver.find_element(
        #     By.XPATH, '//div[@id="tw-target-text-container"]//span')
        # print("*"*50, output_text.text)
        time.sleep(1)
        output_text = driver.find_element(
            By.XPATH, '//div[@id="gt-src-is"]//div[@class="gt-is-lb"]/div')
        # By.XPATH, '//div[@id="tw-target-text-container"]//span')
        output_text_value = output_text.text
        # print("*"*50, output_text_value)
        print(
            f"{i} ==> {type(output_text_value)}  |  {output_text_value[:15]}")

        out_csv.append(output_text_value)

        # for i in out_csv:
        #     with open("output_xl5.csv", "ab") as file:
        #         foo = f"\"{i}\",\n"
        #         file.write(foo.encode('utf-8'))

        with open(output_csv_file, "ab") as file:
            foo = f"\"{out_csv[0]}\",\n"
            file.write(foo.encode('utf-8'))

        time.sleep(.3)

    except:
        print(f"{i} ==> expection", "="*20)
        with open(output_csv_file, "ab") as file:
            foo = f"\"\",\n"
            file.write(foo.encode('utf-8'))
        continue


# time.sleep(300)
driver.close()