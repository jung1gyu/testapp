from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://kafun.taiki.go.jp/Hyou0.aspx?MstCode=51310200&AreaCode=03")  

bsObject = BeautifulSoup(html, "html.parser") 


#print(bsObject.title)
#print(bsObject) 
print(bsObject.main) 