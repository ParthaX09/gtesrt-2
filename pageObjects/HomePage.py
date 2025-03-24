from Locators.HomeLoc import HomeLoc
from utilities.Wait import Wait


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    def click_sent(self):
        btn = Wait.ec(self.driver, HomeLoc.sent)
        btn.click()


    def click_more(self):
        btn = Wait.ec(self.driver, HomeLoc.more)
        assert btn.is_displayed(), "Button not displayed"
        btn.click()


    def click_trash(self):
        btn = Wait.ec(self.driver, HomeLoc.trash)
        assert btn.is_displayed(), "Trash not visible"
        btn.click()


