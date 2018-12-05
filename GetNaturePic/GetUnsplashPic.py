import re
import urllib.request
from GetLinkDataDyc import GetLinkDataDycCls

class GetUnsplashPic(GetLinkDataDycCls):
    def __init__(self):
        GetLinkDataDycCls.__init__(self)
    
    def GetClassTypeUrl(self,url):
        clslist=[]
        driver=self.GetDefaultDriver()
        if driver:
            driver.get(url)
            clslist=self.GetUserLinkData(driver,self.GetClassTypeFilter)  
        return clslist

    def RemoveRepeatData(self,ls):
        list1=[]
        for item  in ls:
            if item not in list1:
               list1.append(item)
        ls=list1

    def GetClassTypeFilter(self,linkstr,ls):
        reg = r'(/t/.+?)'
        clsre = re.compile(reg)
       
        hrefls=clsre.findall(linkstr)
        if hrefls:
           ls.append(linkstr)

    def GetImageUrlFilter(self,linkstr,ls):
        reg = r'(https://unsplash\.com/photos/.+?download\?force=true)'
        clsre = re.compile(reg)
        print(linkstr)
        hrefls=clsre.findall(linkstr)
        self.Show(hrefls)
        if hrefls:
           ls.append(hrefls[0])

    def GetWebData(self,url,getpath):
        clsurls= self.GetClassTypeUrl(url)
        self.RemoveRepeatData(clsurls)
        self.Show(clsurls)
        for clsurl in clsurls:
            print(clsurl)
            driver=self.GetDataDefaultDriver(clsurl)
            imagelist=self.GetUserLinkData(driver,self.GetImageUrlFilter,10)
            self.RemoveRepeatData(imagelist)
            self.Show(imagelist)
            paths=getpath(clsurl)
            self.MakePics(imagelist,paths)

    def Show(self,ls):
       index=1
       for li in ls:
           print(index,li) 
           index=index+1   
    
    def MakePic(self,imgurl,paths,ncount):
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,ncount))

    def MakePics(self,imglist,paths):
        index=1
        for imgurl in imglist:

            self.MakePic(imgurl,paths,index)
            index=index+1


    def Test(self):
        print("GetUnsplashPic")    


if __name__ == "__main__":
     ts = GetUnsplashPic()
     ts.Test()