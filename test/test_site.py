from selenium.webdriver.common.by import By

import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):

    homepage = HomePage(browser)
    homepage.open()
    homepage.click_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


def test_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    #browser.get('https://www.demoblaze.com/index.html')
    #monitor_link = browser.find_element(By.CSS_SELECTOR,'''[onclick="byCat('monitor')"]''')
    #monitor_link.click()
    time.sleep(2) #shit
    homepage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    #assert len(monitors) == 2