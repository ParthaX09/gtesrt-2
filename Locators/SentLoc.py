from selenium.webdriver.common.by import By


class SentLoc:
    smail = (By.XPATH, "//tbody/tr/td/div[text()='To: ']/span[text()][1]")
    advsearch = (By.XPATH, "//span[text()='Advanced search']")
    stext = (By.XPATH, "//div[contains(text(),'Python')]")