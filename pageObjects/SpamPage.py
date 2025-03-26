from Locators.SpamLoc import SpamLoc
from utilities.Wait import Wait


class SpamPage:
    def __init__(self, driver):
        self.driver = driver


    def checkPage(self):
        try:
            text = Wait.pe(self.driver, SpamLoc.assertText)
            assert "Spam" in text.text, "Spam not opened"
        except Exception as e:
            print(f"{e}")



