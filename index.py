from urllib.request import urlopen  # 인터넷 url를 열어주는 패키지
from urllib.parse import quote_plus  # 한글을 유니코드 형식으로 변환해줌
from bs4 import BeautifulSoup
from selenium import webdriver  # webdriver 가져오기
import time  # 크롤링 중 시간 대기를 위한 패키지
import warnings  # 경고메시지 제거 패키지
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings(action='ignore')  # 경고 메세지 제거


baseUrl = 'https://www.instagram.com/'
plusUrl = input('input the inst ID : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

login_section = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
driver.find_element_by_xpath(login_section).click()
time.sleep(2)


elem_login = driver.find_element_by_name("username")
elem_login.clear()
elem_login.send_keys('hainho9704@gmail.com')

elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys('123123z')

time.sleep(1)

xpath = """//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button"""
driver.find_element_by_xpath(xpath).click()

time.sleep(4)


driver.get(url)

time.sleep(3)

numOfPagedowns = 5

body = driver.find_element_by_tag_name("body")

while(numOfPagedowns > 0):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    numOfPagedowns -= 1


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

insta = soup.select('.v1Nh3.kIKUG._bz0w')

saveSpace = './4700k/'

n = 1
for i in insta:

    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open(saveSpace + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
j = 0
for j in range(0, 7):
    time.sleep(3)

    numOfPagedowns = 8

    while(numOfPagedowns > 0):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        numOfPagedowns -= 1

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    insta = soup.select('.v1Nh3.kIKUG._bz0w')

    for i in insta:

        imgUrl = i.select_one('.KL4Bh').img['src']
        with urlopen(imgUrl) as f:
            with open(saveSpace + plusUrl + str(n) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1
    j += 1

driver.close()
