from selenium.webdriver.common.by import By


class TrashLoc:
    trashText = (By.XPATH, "//div[contains(text(),'Messages')]")
    emptyText = (By.XPATH, "//span[contains(text(),'Empty')]")
    confirmText = (By.XPATH, "//span[contains(text(),'OK')]")