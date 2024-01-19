from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
count = 0

common_option = webdriver.ChromeOptions()
common_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=common_option)

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
class InstaFollower:
    def __init__(self):
        self.driver = driver
        self.count = 0

    def login(self,USER, PASS):
        # log into account with username passed and password
        self.driver.get(url=INSTAGRAM_URL)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(USER, Keys.ENTER)
        time.sleep(3)
        # we input our password
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(PASS, Keys.ENTER)
        time.sleep(4)
        # we click the not now save login
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        time.sleep(3)
        # we don't want notification
        self.driver.find_element(By.XPATH, "// button[contains(text(), 'Not Now')]").click()
        time.sleep(3)
        print("completed login, going to find followers........")

    # search for follower
    def findfollowers(self, to_search):
        # The name of the person you want to search will be after the instagram url
        self.driver.get(f"https://www.instagram.com/{to_search}/")
        time.sleep(3)

        #we search for the followers
        self.driver.find_element(By.XPATH, f"//a[@href='/{to_search}/followers/']").click()

        time.sleep(2)

        names = self.driver.find_elements(By.XPATH, "//div[@class='_aano']")

        for i in range(len(names)-1,0,1):
            self.count += 1
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", names)
            print(f"{self.count} : ......." )
            self.follow()

            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in all_buttons:

            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                error = self.driver.find_element(By.XPATH,"//button[@class='_a9-- _ap36 _a9_1']")
                time.sleep(2)
                error.click()
                time.sleep(2)
        # finally:
        #     self.driver.find_element(By.XPATH,
        #                              "//div[10]//div[1]//div[1]//div[1]//div[3]//div[1]//button[1]//div[1]//div[1]").click()
        #     time.sleep(2)







