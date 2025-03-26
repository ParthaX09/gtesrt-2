from selenium.webdriver.common.by import By


class LabelLoc:
    labelbox = (By.XPATH, "//input[@aria-invalid='false']")
    create = (By.XPATH, "//span[contains(text(),'Create')]")