from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Automation:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def setup(self):
        self.driver.get("https://testpages.herokuapp.com/")
        assert self.driver.find_element(By.XPATH, "/html/body/div/h1").text == "Test Pages For Automating"

    def shutdown(self):
        self.driver.close()


o = Automation()
o.setup()
# o.shutdown()
