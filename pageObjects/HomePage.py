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


    def click_add(self):
        try:
            btn = Wait.ec(self.driver, HomeLoc.addlabel)
            assert btn.is_displayed()
            btn.click()
        except Exception as e:
            print(f"{e}")


    def click_spam(self):
        btn = Wait.ec(self.driver, HomeLoc.spam)
        btn.click()


    def click_important(self):
        btn = Wait.ec(self.driver, HomeLoc.important)
        btn.click()


    def click_scheduled(self):
        btn = Wait.ec(self.driver, HomeLoc.scheduled)
        btn.click()


    def check_label(self):
        try:
            btn = Wait.pe(self.driver, HomeLoc.findlabel)
            assert btn.is_displayed(), "Label not present"
        except Exception as e:
            print(f"{e}")

