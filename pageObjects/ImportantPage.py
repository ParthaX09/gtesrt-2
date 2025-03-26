from Locators.ImpotantLoc import ImportantLoc
from utilities.Wait import Wait


class ImportantPage:
    def __init__(self, driver):
        self.driver = driver


    def assert_page(self):
        try:
            btn = Wait.pe(self.driver, ImportantLoc.fromtext)
            assert btn.is_displayed(), "Button not present"
        except Exception as e:
            print(f"{e}")