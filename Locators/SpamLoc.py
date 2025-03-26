from selenium.webdriver.common.by import By


class SpamLoc:
    assertText = (By.XPATH, "//div[contains(text(),'automatically deleted')]")