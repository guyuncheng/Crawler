# 
from selenium import webdriver
import time
import re

driver = webdriver.PhantomJS(".//phantomjs.exe")
driver.get("https://unsplash.com/t/nature")
 
# 向下滚动10000像素
js = "document.body.scrollTop=100000"
js="var q=document.documentElement.scrollTop=document.documentElement.scrollHeight"
 
time.sleep(10)
 
#查看页面快照
# driver.save_screenshot("douban.png")
 
# 执行JS语句
#driver.execute_script(js)
counter = 1
n = 10
while counter <= n:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)");
    time.sleep(10)
    counter += 1


#查看页面快照
# driver.save_screenshot("newdouban.png")
#  driver.find_elements_by_xpath()
hrefls=[]
imglist=[]

reg = r'(https://unsplash\.com/photos/.+?download\?force=true)'
imgre = re.compile(reg)
index=1

for link in driver.find_elements_by_xpath("//a[@href]"):
   
 
    print (link.get_attribute('href'))
    # index=index+1
    
    hrefls=imgre.findall(link.get_attribute('href'))
    if hrefls:
       imglist.append(hrefls)
    
list1=[]
for item  in imglist:
    if item not in list1:
       list1.append(item)
imglist=list1
for imgurl in imglist:  
    print(index,imgurl)
    index=index+1 
driver.quit()



