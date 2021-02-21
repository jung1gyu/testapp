
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='/Users/wongyujung/Desktop/vsproject/testapp/chromedriver')
driver.get("http://kafun.taiki.go.jp/Hyou0.aspx?MstCode=51310200&AreaCode=03")
driver.implicitly_wait(10)

#r = driver.page_source
#soup = BeautifulSoup(r, "html.parser")

driver.switch_to.frame("main")
r1 = driver.page_source
soup1 = BeautifulSoup(r1, "html.parser")

#print(soup1) 
print(soup1.head.title)

#pip install pipenv
#pipenv shell
#pipenv install selenium
#xattr -d com.apple.quarantine /usr/local/bin/chromedriver


