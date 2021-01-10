import requests
import parsel
from lxml import etree
from selenium  import webdriver
import time
import csv
import re

def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    product = {}
    product_all = {}
    with open('data.csv','a',newline='') as filecsv:
        csvwriter = csv.writer(filecsv,delimiter = ',')
        for id_product,div in enumerate(divs):
            product['info'] = div.find_elements_by_xpath('.//div[@class="row row-2 title"]')[0].text
            product['price'] = div.find_elements_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong')[0].text+'元'
            product['Number_of_people'] = div.find_elements_by_xpath('.//div[@class="deal-cnt"]')[0].text
            product['address'] = div.find_elements_by_xpath('.//div[@class="location"]')[0].text
            product['Shop'] = div.find_elements_by_xpath('//div[@class="shop"]/a/span[2]')[0].text
         #   with open('data.csv','a',newline='') as filecsv:
         #       csvwriter = csv.writer(filecsv,delimiter = ',')
            csvwriter.writerow([product['info'],product['price'],product['Number_of_people'],product['Shop'],product['address']])
      #  product_all[id_product] = product
   # return product_all

def search_product(keywords):
    driver.find_element_by_id('q').send_keys(keywords)
    driver.find_element_by_class_name('btn-search').click()
    driver.maximize_window()
    time.sleep(15)

    page = driver.find_elements_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]')[0].text
    page = re.findall('(\d+)',page)[0]             #提取page中的数字
    return int(page)

keywords = '高跟鞋'
while 1:
    try:
        driver = webdriver.Chrome()
        break
    except:
        time.sleep(1)
driver.get('https://www.taobao.com/')
page = search_product(keywords)
with open('data.csv','a',newline='') as filecsv:
    csvwriter = csv.writer(filecsv,delimiter = ',')
    csvwriter.writerow(['商品名称','商品价格','付款人数','店铺','发货地址'])
    get_product()
    page_num = 1
  #  page = 2
    while page_num != page:
        print('正在爬取第'+str(page_num)+'页数据')
        driver.get('https://s.taobao.com/search?q='+keywords+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s='+str(page_num*44))
        driver.implicitly_wait(2)                      #浏览器等待 因为爬取速度过快
        driver.maximize_window()                       #浏览器最大化
        get_product()
        page_num = page_num+1
a = 1














'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
url = 'https://uland.taobao.com/sem/tbsearch?spm=a2e15.8261149.07626516003.2.217929b4Quq6Gx&refpid=mm_15891853_2192459_8654707&clk1=e6b025aa18443c9c691333db67d383d6&keyword=%E9%AB%98%E8%B7%9F%E9%9E%8B&page=1&_input_charset=utf-8'
response = requests.get(url = url, headers = headers)
response.encoding = response.apparent_encoding                              #请求网页，获取网页数据
data = response.text
sel = parsel.Selector(data)  
Fund_manager = sel.xpath('//*[@id="ItemWrapper"]/div[1]/a/div[2]/span').get()
a = 1
'''