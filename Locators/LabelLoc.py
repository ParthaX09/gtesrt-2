from selenium.webdriver.common.by import By


# contains all the locators for the label page
class LabelLoc:
    labelbox = (By.XPATH, "//input[@aria-invalid='false']")
    create = (By.XPATH, "//span[contains(text(),'Create')]")