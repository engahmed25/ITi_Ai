
from selenium import webdriver
import csv



PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://egypt.souq.com/eg-en/samsung/mobile-phones-33%7Csmart-watches-511%7Ctablets-94%7Cfitness-technology-498%7Cpower-banks-562/samsung/a-t-7/s/?_=1500309575629&sortby=sr&ref=nav&section=2&page=1')

products = driver.find_elements_by_xpath("//h1[@class='itemTitle']")
prices = driver.find_elements_by_xpath("//h3[@class='itemPrice']")


for product in products:
    print(product.text)


for product_price in prices:
    print(product_price.text)
    
    
with open('D:\Souq_Products.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Product Name','Price'])
    for i in range(1,len(products)):
        csvwriter.writerow([products[i].text,prices[i].text])

    



