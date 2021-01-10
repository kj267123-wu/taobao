import requests
import parsel
from lxml import etree
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'cookie': 'miid=784327266183293985; cna=6iJJE/aMsgcCAXUg2HF16xV+; t=814c291ec8d12e9fbbd7b0d8914cc531; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; sgcookie=EajYmETujJAiBwPzBh4xR; uc3=nk2=oHTG6hgwiCmIVi%2Bh&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=UUwZ%2BvOv76daYg%3D%3D&vt3=F8dBxGynVtJH6%2BR8fG8%3D; lgc=%5Cu68A6%5Cu60F3%5Cu7684%5Cu6628%5Cu592912; uc4=nk4=0%40oibnHwW42sZ3ssWl8ppMb8GRKa8BeVY%3D&id4=0%40U27Gi9URz1jsaS6S0UJY93bEx2gW; tracknick=%5Cu68A6%5Cu60F3%5Cu7684%5Cu6628%5Cu592912; _cc_=WqG3DMC9EA%3D%3D; enc=ood0EDPaUGFOvR55LJ7vxlosoHqflp4bg4n%2FUXyB3d2M0I9CTdEifx2AaxUJRUl6zaqIQonaMzKh6ZNqL8r7sw%3D%3D; mt=ci=21_1; tfstk=cPY5BJ6NF825IzoUzQGVUP9r2S7da1Mfi06JNn-JSfUt2rOVHsjz7OgJwH20kGCf.; _m_h5_tk=3c0c4e0c8043981dc6bccbec4c1cbe7c_1596082019942; _m_h5_tk_enc=38274cf46f7d46d4d0e9cb667f2526f1; cookie2=1a2c1c8e9b13ee3c4a2e90f8437285d5; uc1=cookie14=UoTV6hrOSmazTQ%3D%3D; _tb_token_=5f543b67eeeee; JSESSIONID=78BE10A5563FDFEE80E36695022B50A1; l=eBxdiownqZZG8AZFBO5alurza779eQRfClVzaNbMiInca6Q5saGQ5NQq04DX-dtjgtfA4ety_kJufRewJfU38tgKqelyRs5mpq96-; isg=BLy8zc04z22H1fnQ1_poxLbEjVputWDfVf2w5ZY_eqcbYVnrvsWVblwXQYkZEpg3',
    'referer': 'https://s.taobao.com/search?spm=a230r.1.0.0.6ad92da9szLuNe&q=%E9%AB%98%E8%B7%9F%E9%9E%8B&rs=up&rsclick=1&preq=%E9%AB%98%E8%B7%9F%E9%9E%8B&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=88'
   } 
# 'Referer': 'https://s.taobao.com/search?spm=a230r.1.0.0.6ad92da9szLuNe&q=%E9%AB%98%E8%B7%9F%E9%9E%8B&rs=up&rsclick=1&preq=%E9%AB%98%E8%B7%9F%E9%9E%8B&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0'
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'} 
#url = 'https://s.taobao.com/search?spm=a230r.1.0.0.6ad92da9szLuNe&q='+'高跟鞋'+'&rs=up&rsclick=1&preq=%E9%AB%98%E8%B7%9F%E9%9E%8B&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44'
url = 'https://s.taobao.com/search?data-key=s%2Cps&data-value=0%2C1&ajax=true&_ksTS=1596069276185_1011&callback=jsonp1012&spm=a230r.1.0.0.6ad92da9szLuNe&q=%E9%AB%98%E8%B7%9F%E9%9E%8B&rs=up&rsclick=1&preq=%E9%AB%98%E8%B7%9F%E9%9E%8B&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=88'
response = requests.get(url = url,headers = headers) 
'''
text = response.content.decode('utf-8')
html = etree.HTML(text)
ul = html.xpath('/html/body/div[1]/div[2]/div[3]')[0]
'''
response.encoding = response.apparent_encoding                              #请求网页，获取网页数据
html = response.text
#html_new=html.replace(r'<!--','"').replace(r'-->','"')
'''
content=etree.HTML(html_new)
result=content.xpath('//div[@class="threadlist_title pull_left j_th_tit "]//a[@rel="noreferrer"]/@href')
a = 1
'''
sel = parsel.Selector(html)  #ItemWrapper > div:nth-child(1) > a > div.info > span
Fund_manager = sel.xpath('//div[@class="row row-3 g-clearfix"]').get()
a=1
'''
html  = response.content
data = etree.HTML(html).xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div[1]/div[2]/div[2]/a')
a = 1
'''