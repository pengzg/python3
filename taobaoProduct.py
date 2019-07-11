from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


def get_one_page(page):
    """
    抓取索引页
    :param page:页码
    """
    print('正在抓取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        get_one_page(page)




def get_products():
    print(1111)
    """
    提取商品
    """
    html = browser.page_source
    doc=pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for pitem in items:
        product = {
            'title':pitem.find('.J_ItemPic').attr('alt'),
            'img':pitem.find('.J_ItemPic').attr('data-src'),
            'price':pitem.find('.price strong').text(),
            'shop':pitem.find('.shopname span:nth-child(2)').text(),
            'location':pitem.find('.location').text()

        }

        print(product)

MAX_PAGE = 2
def main():
    for i in range(1, MAX_PAGE+1):
        get_one_page(i)


main()

