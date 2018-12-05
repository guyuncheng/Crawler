class CGetMeiTuanCityShops(object):
    def GetShops(self,driver,url,dictShop):
        if driver:
            driver.get(url)
            shopsElem=driver.find_element_by_class_name("category-nav-content-wrapper")
            Shops=shopsElem.find_elements_by_xpath(".//*[@href]")
            for  Shop in Shops:
                 dictShop[Shop.text]=Shop.get_attribute('href')
