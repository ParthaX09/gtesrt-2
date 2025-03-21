from Locators.SentLoc import SentLoc
from utilities.Wait import Wait


class SentPage:
    def __init__(self, driver):
        self.driver = driver


    def check_pageOpen(self):
        btn = Wait.pe(self.driver, SentLoc.advsearch)
        assert btn.is_displayed(), "Sent page not opened"


    def check_mail(self):
        ids = self.driver.find_elements(*SentLoc.smail)
        id = None
        for id in ids:
            if "me" in id.text:
                break
        else:
            print("Mail not found")

