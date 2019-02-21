# TestSelenium.py

#!/user/bin/env python
#encoding: utf-8

from selenium import webdriver

chrome_driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver_path)
browser.get("https://120.27.83.26:8085/QuyiAdmConsole/")
print(browser.title)

browser.find_element_by_id("user_id").send_keys("admin")
browser.find_element_by_id("user_pwd").send_keys("qy123456")
browser.find_element_by_xpath('//*[@id="nLogin"]/table/tbody/tr[2]/td/button').click()
browser.implicitly_wait(5)
browser.find_element_by_xpath('//*[@id="_easyui_tree_67"]/span[4]').click()
browser.implicitly_wait(5)
elementi = browser.find_element_by_xpath('//*[@id="centerTabs"]/div[2]/div/div/iframe')
browser.switch_to.frame(elementi)
browser.find_element_by_xpath('//*[@id="searchform"]/table/tbody/tr[1]/td[4]/span').click()
browser.find_element_by_xpath('//*[@id="_easyui_combobox_i1_1"]').click()
a = browser.find_element_by_xpath('//*[@id="searchform"]/table/tbody/tr[2]/td[5]/a')
browser.implicitly_wait(5)
a.click()

