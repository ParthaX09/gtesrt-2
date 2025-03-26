from Locators.TrashLoc import TrashLoc
from utilities.Wait import Wait


class TrashPage:
    def __init__(self, driver):
        self.driver = driver


    def isTrashOpen(self):
        text = Wait.pe(self.driver, TrashLoc.trashText)
        assert text.is_displayed(), "Trash not opened"


    def del_mail(self):
        try:
            btn = Wait.pe(self.driver, TrashLoc.emptyText)
            btn.click()
            TrashPage.click_del()
        except Exception:
            print(Exception)

    def click_del(self):
        try:
            btn = Wait.ec(self.driver, TrashLoc.confirmText)
            assert  btn.is_displayed(), "No button"
            btn.click()
        except Exception:
            print(Exception)
