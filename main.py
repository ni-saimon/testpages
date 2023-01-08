from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def wait():
    while True:
        pass


class Automation:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def setup(self):
        self.driver.get("https://testpages.herokuapp.com/")
        assert self.driver.find_element(By.XPATH, "/html/body/div/h1").text == "Test Pages For Automating"

    def basic_web_page_example(self):
        self.driver.find_element(By.ID, "basicpagetest").click()
        print(self.driver.find_element(By.CSS_SELECTOR, "h1").text)
        print(self.driver.find_element(By.CSS_SELECTOR, "div[class='explanation'] p").text)
        print(self.driver.find_element(By.CSS_SELECTOR, "p[id='para1']").text)
        print(self.driver.find_element(By.CSS_SELECTOR, "p[id='para2']").text)

    def shutdown(self):
        self.driver.close()


o = Automation()
o.setup()
o.basic_web_page_example()
wait()
# o.shutdown()
