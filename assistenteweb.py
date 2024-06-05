from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
barra=input("cosa vuoi cercare?: ")


chrome_driver = ChromeDriverManager().install()
driver= Chrome(service=Service(chrome_driver))
driver.get(barra)
driver.maximize_window()

sleep(2)
