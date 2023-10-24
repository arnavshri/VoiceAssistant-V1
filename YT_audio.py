from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class music():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(executable_path='E:\Setups\chromedriver-win64\chromedriver-win64\chromedriver.exe') 
        self.driver = webdriver.Chrome(service=service , options=options)

    def play(self, query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element("xpath",'//*[@id="video-title"]')
        video.click()
    
# assist = music()
# assist.play('king zayde wolf')