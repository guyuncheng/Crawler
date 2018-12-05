
class CGetMeiTuanCities(object):
    def GetCities(self,driver,url,dictCities):
        if driver:
            driver.get(url)
            citiesElems=driver.find_elements_by_class_name("cities")
            for citiesElem in citiesElems:
                Cities=citiesElem.find_elements_by_xpath(".//*[@href]")
                for city in Cities:
                    dictCities[city.text]=city.get_attribute('href')