from selenium import webdriver
import time
import re
dictCities={}
#driver = webdriver.PhantomJS(".//phantomjs.exe")
driver=webdriver.Firefox()
driver.get("https://www.meituan.com/changecity/")
citiesElems=driver.find_elements_by_class_name("cities")
for citiesElem in citiesElems:
    Cities=citiesElem.find_elements_by_xpath(".//*[@href]")
    for city in Cities:
        dictCities[city.text]=city.get_attribute('href')

for key,val in dictCities.items():
    print(key,val)

for key,val in dictCities.items():
   driver.get(val)
   break


 