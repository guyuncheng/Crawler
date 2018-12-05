from selenium import webdriver
from GetMeiTuanCities import CGetMeiTuanCities
from GetMeiTuanCityShop import CGetMeiTuanCityShops

dictCities={}
dictShops={}
driver=webdriver.PhantomJS(".//phantomjs.exe")
getCities=CGetMeiTuanCities()
getCities.GetCities(driver,"https://www.meituan.com/changecity/",dictCities)
for key,val in dictCities.items():
    getShops=CGetMeiTuanCityShops()
    getShops.GetShops(driver,val,dictShops)

for key,val in dictShops.items():
    print(key,val)
    
    