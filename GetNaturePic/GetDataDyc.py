
from selenium import webdriver
import time

class GetDataDycCls:
    def __init__(self):
         self._driver=webdriver.PhantomJS(".//phantomjs.exe")
         self._url=""

    def __del__(self):
        if self._driver:
            self._driver.quit()

    def SetDriver(self,driver):
        self._driver=driver

    def SetUrl(self,url):
        self._url=url

    def GetDefaultDriver(self):
        if self._driver:
            return self._driver
        else:
            self._driver=webdriver.PhantomJS()
            return self._driver

    def GetDefaultData(self):
        driver=self.GetDefaultDriver()
        if driver:
           driver.get(self._url)

    def GetDataDefaultDriver(self,url):
        driver=self.GetDefaultDriver()
        if driver:
           driver.get(url)
        return driver
        

    def GetDataDriver(self,driver,url):
        if driver:
           driver.get(url)    
    
    def GetData(self,driver,nCount):
        if driver:
           counter = 1
           while counter <= nCount:
                 driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                 time.sleep(10)
                 counter += 1

        return driver
    def Test(self):
        print("GetDataDycCls")    
if __name__ == "__main__":
     ts = GetDataDycCls()
     ts.Test()