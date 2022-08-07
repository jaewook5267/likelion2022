from time import time
from selenium import webdriver
from bs4 import BeautifulSoup

#파일이 실행될 떄 환경변수에 현재 자신의 프로젝트의 settings.py파일 경로를 등록해줘야 한다.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myproject.settings")

#실행파일에 Django 환경을 불러온다.
import django
django.setup()

#우리 상품모델에 저장해야되서 import해오기
from shop.models import *


# -------크롤링 전 간단설명----------
# 원래는 beautifulsoup라이브러리만을 사용해서 크롤링작업을 하려고했으나 해당사이트에 있는 상품목록들이 javascript상으로 동적처리가 
# 돼있는지,, beautifulsoup으로 크롤링인 안됨. 그래서 selenium라이브러리를 이용해서 접근함.

# 우리가 긁어와야하는 상품이 총 84개인데, 총 3페이지에 걸쳐서 나열돼있다.--> 동적처리에 유연한 selenium을 사용해서 [다음페이지]를 눌러주면서 다 긁어옴.



#크롤링함수 선언
def dbsave():
    
    #selenium을사용해서 브라우저열기
    driver = webdriver.Chrome("C:\chromedriver")
    driver.get('https://mustit.co.kr/product/search?search_action=search&event=0&event_no=1004&keyword=%EA%B0%95%EC%95%84%EC%A7%80%20%EC%9A%A9%ED%92%88&x=0&y=0&search_count=0&click=all_productsearch')
    
    #받아올 것들 리스트 생성
    imglist=[]
    brandlist=[]
    namelist=[]
    pricelist=[]

    #창은 selenium으로 열되, 데이터파싱은 beautifulsoup으로 한다. 
    #그 이유는, selenium은 동적인 환경에서 우리가 원하는 부분을 얻을 수 있기 때문에 좋은 도구지만 파싱속도가 매우 느리다. 
    #--------------여기서부터 1페이지 크롤링 시작------------------
    soup = BeautifulSoup(driver.page_source,"lxml")
    
    elements = soup.select(
        '#view_gallery > div > div > div.mi-card-product-2'
    )

    for el in elements:
        el_img = el.select_one('a > span.mi-card-product-image-2 > img').get("src")
        el_brand = el.select_one('a > span.product-desc-box > h5 > span').get_text()
        el_name = el.select_one('a > span.product-desc-box > p').get_text()
        el_price = el.select_one('a > span.product-desc-box > span > span').get_text()
        imglist.append(el_img)
        brandlist.append(el_brand)
        namelist.append(el_name)
        pricelist.append(el_price)

    #다음페이지 클릭
    driver.find_element_by_css_selector("#normal_list > div.mi-pagination > ul > li:nth-child(2) > a").click()


    #--------------여기서부터 2페이지 크롤링 시작------------------
    soup = BeautifulSoup(driver.page_source,"lxml")
    elements2 = soup.select(
        '#view_gallery > div > div > div.mi-card-product-2'
    )
    for el in elements2:
        el_img = el.select_one('a > span.mi-card-product-image-2 > img').get("src")
        el_brand = el.select_one('a > span.product-desc-box > h5 > span').get_text()
        el_name = el.select_one('a > span.product-desc-box > p').get_text()
        el_price = el.select_one('a > span.product-desc-box > span > span').get_text()
        imglist.append(el_img)
        brandlist.append(el_brand)
        namelist.append(el_name)
        pricelist.append(el_price)

    #다음페이지 클릭
    driver.find_element_by_css_selector("#normal_list > div.mi-pagination > ul > li:nth-child(3) > a").click()




    #--------------여기서부터 3페이지 크롤링 시작------------------
    soup = BeautifulSoup(driver.page_source,"lxml")
    elements3 = soup.select(
        '#view_gallery > div > div > div.mi-card-product-2'
    )
    for el in elements3:
        el_img = el.select_one('a > span.mi-card-product-image-2 > img').get("src")
        el_brand = el.select_one('a > span.product-desc-box > h5 > span').get_text()
        el_name = el.select_one('a > span.product-desc-box > p').get_text()
        el_price = el.select_one('a > span.product-desc-box > span > span').get_text()
        imglist.append(el_img)
        brandlist.append(el_brand)
        namelist.append(el_name)
        pricelist.append(el_price)



    #이제 리스트에있는 것들을 하나씩 다 꺼내서 모델에 저장
    for i,j,l,m in zip(imglist, brandlist, namelist, pricelist):
     
        if "조끼" in l:
            c = Category.objects.get(name='조끼')
        elif "신발" in l:
            c = Category.objects.get(name='신발')
        elif "자켓" in l:
            c = Category.objects.get(name='자켓')            
        elif "영양제" in l:
            c = Category.objects.get(name='영양제')
        elif "비타민" in l:
            c = Category.objects.get(name='영양제')
        elif "베드" in l:
            c = Category.objects.get(name='베드')
        elif "리드줄" in l:
            c = Category.objects.get(name='리드줄')
        elif "목줄" in l:
            c = Category.objects.get(name='목줄')
        elif "코트" in l:
            c = Category.objects.get(name='코트')            
        else:
            c = Category.objects.get(name='기타')

        p = Product()
        p.category= c 
        p.img = i
        p.brand = j
        p.name = l
        p.price = int(m.replace(",",""))
        p.description = "크롤링한 상품입니다."  
        p.pub_date = timezone.now()
        p.is_crolled = True
        p.save()



    #selenium테스트 종료
    driver.quit()


#함수실행
dbsave()







