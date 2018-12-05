import os
from GetUnsplashPic import GetUnsplashPic

def GetPath(url):
    path=".\\pic\\"
    dir=""
    index=url.rfind('/')
    dir=url[index+1:-1]
    path=path+dir
    if not os.path.isdir(path):  
        os.makedirs(path) 
    return path+"\\"

pic=GetUnsplashPic() 
pic.GetWebData("https://unsplash.com/",GetPath)

