# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #鼠标
from selenium.webdriver.common.keys import Keys  #键盘
import time
from selenium.webdriver.support.ui import WebDriverWait

geckodriver='G:/Python_project/geckodriver.exe'
driver = webdriver.Firefox(executable_path=geckodriver)
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('博客园1')
#键盘删除
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
driver.find_element_by_id('su').click()

driver.maximize_window()
window = driver.window_handles
driver.find_element_by_xpath("//h3[@class='t']/a").click()
time.sleep(3)
window = driver.window_handles
driver.switch_to.window(window[1])

#双击
double = driver.find_element_by_xpath("//*[@id='logo']/h1/a")
ActionChains(driver).double_click(double)
#等待
driver.implicitly_wait(3)
time.sleep(3)
element = WebDriverWait(driver,10,0.5).until(lambda driver:driver.find_element_by_xpath("//*[@id='nav_menu']/a[1]"))
element.click()
title = driver.title
url = driver.current_url
print(title, url)

#退出
driver.close()