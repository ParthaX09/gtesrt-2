from selenium.webdriver.common.by import By

# contains all the locators for the important page
class LoginLoc:
    emailid = (By.XPATH, "//input[@id='identifierId']")
    next = (By.XPATH, "//span[text()='Next']")
    pswd = (By.XPATH, "//input[@type='password']")