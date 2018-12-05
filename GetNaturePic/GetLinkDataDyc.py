from GetDataDyc import GetDataDycCls

class GetLinkDataDycCls(GetDataDycCls):

    def __init__(self):
       GetDataDycCls.__init__(self)
    
    def GetLinkData(self,driver,ncount=0):
        if driver:
           self.GetData(driver,ncount)
           elems=driver.find_elements_by_xpath("//*[@href]")
        return elems
    
    def GetUserLinkData(self,driver,func,ncount=0):
        linklist=[]
        elems=self.GetLinkData(driver,ncount)
        if elems:
            for elem in elems:
                func(elem.get_attribute('href'),linklist)
        return linklist

    def Test(self):
        print("GetLinkDataDycCls")    
if __name__ == "__main__":
     ts = GetLinkDataDycCls()
     ts.Test()
        
        