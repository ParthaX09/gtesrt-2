from Locators.HomeLoc import HomeLoc
from utilities.Wait import Wait


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    def click_sent(self):
        btn = Wait.ec(self.driver, HomeLoc.sent)
        btn.click()


    def click_more(self):
        pass


    def click_trash(self):
        pass


