from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wait:
    def ec(driver, locator):
        btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        return btn


    def pe(driver, locator):
        btn = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(locator)
        )
        return btn