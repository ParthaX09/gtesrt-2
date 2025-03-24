from Locators.TrashLoc import TrashLoc
from utilities.Wait import Wait


class TrashPage:
    def __init__(self, driver):
        self.driver = driver


    def isTrashOpen(self):
        text = Wait.pe(self.driver, TrashLoc.trashText)
        assert text.is_displayed(), "Trash not opened"