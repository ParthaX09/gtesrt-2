import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_Main(BaseClass):
    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.checkImg()


    def test_compose(self):
        pass
