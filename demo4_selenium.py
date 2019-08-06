from selenium import webdriver

#实例化一个浏览器驱动
chrome = webdriver.Chrome()

#访问界面
chrome.get("https://www.baidu.com/")

#捕获元素
inputs = chrome.find_element_by_id("kw")

#对元素进行操作
inputs.send_keys("大娘水饺")

button = chrome.find_element_by_id("su")

button.click()

#关闭浏览器
chrome.close()
