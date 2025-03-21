from Locators.ComposeLoc import ComposeLoc
from utilities.Wait import Wait


class ComposePage:
    def __init__(self, driver):
        self.driver = driver


    def clickCompose(self):
        btn = Wait.ec(self.driver, ComposeLoc.compose)
        btn.click()


    def get_to(self, email):
        box = Wait.ec(self.driver, ComposeLoc.to)
        box.send_keys(email)


    def get_sub(self):
        box = Wait.ec(self.driver, ComposeLoc.sub)
        box.send_keys("Hello")


    def get_desc(self):
        box = Wait.ec(self.driver, ComposeLoc.desc)
        box.send_keys("Gmail Automation using selenium")


    def click_send(self):
        btn = Wait.ec(self.driver, ComposeLoc.send)
        btn.click()


    def check_sent(self):
        alert = Wait.pe(self.driver, ComposeLoc.msg)
        assert alert.is_displayed(), "Message not sent"