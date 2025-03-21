from selenium.webdriver.common.by import By


class ComposeLoc:
    compose = (By.XPATH, "//div[contains(text(), 'Compose')]")
    to = (By.XPATH, "//input[@aria-label='To recipients']")
    sub = (By.XPATH, "//input[@name='subjectbox']")
    desc = (By.XPATH, "//div[@role='textbox']")
    send = (By.XPATH, "//div[@aria-label='Send ‪(Ctrl-Enter)‬']")
    msg = (By.XPATH, "//span[text()='Message sent']")