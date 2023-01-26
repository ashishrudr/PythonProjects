from time import sleep

from selenium import webdriver
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--incognito')
#driver=webdriver.Chrome(executable_path="C:/Users/rudra/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1861837845%3A1672508920464484&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh7Y9fMqdWLaHsFZE-EqLa67E4ISuQcnc8Cf8u65hb3imMN90RNwvekxErtOR0KtJ7vJSKOTYw")
driver.find_element('xpath',"//input[@type='email']").send_keys("awesumrudr")
sleep(8)
driver.find_element('xpath', "//span[text()='Next']/parent::button").click()
sleep(8)
driver.find_element('xpath',"//input[@type='password']").send_keys("shilasingh")


