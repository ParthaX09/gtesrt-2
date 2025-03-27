from selenium.webdriver.common.by import By


# contains all the locators for the important page
class ImportantLoc:
    fromtext = (By.XPATH, "//span[text()='From']")