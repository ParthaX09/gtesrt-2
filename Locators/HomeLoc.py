from selenium.webdriver.common.by import By


#contains all the locators for the home page
class HomeLoc:
    gmailImg = (By.XPATH, "//img[@role='presentation']")
    more = (By.XPATH, "//span[@class='ait']")

    # all the functionalities
    sent = (By.XPATH, "//a[text()='Sent']")
    scheduled = (By.XPATH, "//a[@aria-label='Scheduled']")
    important = (By.XPATH, "//a[@aria-label='Important']")
    spam = (By.XPATH, "//a[@aria-label='Spam']")
    trash = (By.XPATH, "//a[@aria-label='Trash']")

    # all the label functionalities locators
    addlabel = (By.XPATH, "//div[@aria-label='Create new label']")
    labecreated = (By.XPATH, "//div[contains(text(),'created')]")
    findlabel = (By.XPATH, "//a[contains(text(),'L1')]")