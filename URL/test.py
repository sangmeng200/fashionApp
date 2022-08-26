import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = 'https://www.aboutyou.de/p/about-you/chelsea-boots-sophie-3948831'
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
web(1,'https://www.amazon.in/deal/6c8e1c01?showVariations=true&ref=dlx_deals_gd_dcl_img_0_6c8e1c01_dt_sl15_9f')