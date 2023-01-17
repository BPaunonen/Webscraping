from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://hs.fi')

#wait for X seconds
#driver.implicitly_wait(3)

driver.switch_to.frame("sp_message_iframe_755629")

button = driver.find_element(By.CSS_SELECTOR, 'button[tittle="OK"]')
button.click() # automatically presses the button


