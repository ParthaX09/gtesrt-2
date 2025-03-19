from selenium.webdriver.common.by import By


class HomeLoc:
    emailid = (By.XPATH, "//input[@id='identifierId']")
    next = (By.XPATH, "//span[text()='Next']")
    pswd = (By.XPATH, "//input[@type='password']")
    gmailImg = (By.XPATH, "//img[@role='presentation']")