from Locators.ScheduledLoc import ScheduledLoc
from utilities.Wait import Wait


class ScheduledPage:
    def __init__(self, driver):
        self.driver = driver


    def assert_page(self):
        text = Wait.pe(self.driver, ScheduledLoc.assertbox)
        assert text.is_displayed(), "Page not opened"