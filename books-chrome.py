from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = "http://books.toscrape.com"
chrome_options = Options()

chrome_options.add_experimental_option('detach', True)

driver = Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)

driver.get(url)
driver.maximize_window()

query = "//article//a"
results = driver.find_elements("xpath", query)

for result in results:
    if result.tag_name== 'a':
        print(result.get_attribute('title'))