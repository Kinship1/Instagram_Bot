from selenium import webdriver
from time import sleep
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains

class InstaBot:
    def _init_(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(3)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(1)

    def search(self, username):
        self.driver.get("https://instagram.com/"+username)
        sleep(2)
        image = self.driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a").get_attribute('href')
        element_to_hover_over = self.driver.find_element_by_xpath("//div[@class='KL4Bh']")
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@class='qn-0x']").click()
        temp = self.driver.find_elements_by_xpath("//img[@class='FFVAD']")
        print(len(temp))
        for _ in range(23):
            self.driver.get(image)
            sleep(2)
            self.driver.find_element_by_xpath("//a[@class=' _65Bje  coreSpriteRightPaginationArrow']").click()
        for _ in range(23,35):
            self.driver.get(image)
            sleep(2)
            temp = self.driver.find_elements_by_xpath("//img[@class='FFVAD']")
            sleep(2)
            urllib.request.urlretrieve(temp[].get_attribute('src'), str()+".jpg")
            sleep(2)
            self.driver.find_element_by_xpath("//a[@class=' _65Bje  coreSpriteRightPaginationArrow']").click()

username = input("Enter Your Username")
pass = input("Enter Your Password")
usearch = input("Enter Username of the person to be searched")
my_bot = InstaBot(username, pass)
my_bot.search(usearch)