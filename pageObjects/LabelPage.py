from Locators.HomeLoc import HomeLoc
from Locators.LabelLoc import LabelLoc
from utilities.Wait import Wait


class LabelPage:
    def __init__(self, driver):
        self.driver = driver


    def get_label(self):
        try:
            box = Wait.ec(self.driver, LabelLoc.labelbox)
            assert box.is_selected(), "Text box not selected"
            box.send_keys("L1")
        except Exception as e:
            print(f"{e}")

    def create_label(self):
        try:
            btn = Wait.ec(self.driver, LabelLoc.create)
        except Exception as e:
            print(f"{e}")


    def check_created(self):
        try:
            btn = Wait.pe(self.driver, HomeLoc.labecreated)
            assert btn.is_displayed(), "label not created"
        except Exception as e:
            print(f"{e}")

