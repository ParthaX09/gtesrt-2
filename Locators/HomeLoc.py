from selenium.webdriver.common.by import By


class HomeLoc:
    gmailImg = (By.XPATH, "//img[@role='presentation']")
    more = (By.XPATH, "//span[@class='ait']")
    sent = (By.XPATH, "//a[text()='Sent']")
    trash = (By.XPATH, "//a[@aria-label='Trash']")