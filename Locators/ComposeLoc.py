from selenium.webdriver.common.by import By


class ComposeLoc:
    to = (By.XPATH, "//input[@aria-label='To recipients']")
    sub = (By.XPATH, "//input[@name='subjectbox']")
    desc = (By.XPATH, "//div[@role='textbox']")
    send = (By.XPATH, "//div[@aria-label='Send ‪(Ctrl-Enter)‬']")