import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage

driver = None

def pytest_addoption(parser):
    parser.addoption("--email", action="store", help="Login Mail Id")
    parser.addoption("--password", action="store", help="Login Password")


@pytest.fixture(scope="function")
def setup(request):
    global driver

    email = request.config.getoption("--email")
    password = request.config.getoption("--password")

    driver = webdriver.Chrome()
    driver.get("https://www.gmail.com/")
    driver.maximize_window()

    loginPage = LoginPage(driver)
    loginPage.getMail(email)
    loginPage.clickNext()
    loginPage.getPswd(password)
    loginPage.clickNext()

    yield
    driver.quit()


