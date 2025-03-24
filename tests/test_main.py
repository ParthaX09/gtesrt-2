import pytest
from selenium import webdriver

from pageObjects.ComposePage import ComposePage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.SentPage import SentPage
from pageObjects.TrashPage import TrashPage
from utilities.BaseClass import BaseClass


@pytest.fixture(scope="function")
def get_data(self, request):
    email = request.config.getoption("--email")
    return email

@pytest.mark.usefixtures("setup")
@pytest.mark.debug
class Test_Main(BaseClass):

    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.checkImg()


    @pytest.mark.compose
    def test_compose(self, get_data):
        email = get_data
        composePage = ComposePage(self.driver)
        composePage.clickCompose()
        composePage.get_to(email)
        composePage.get_sub()
        composePage.get_desc()
        composePage.click_send()
        composePage.check_sent()


    def test_checkmail(self):
        homePage = HomePage(self.driver)
        sentPage = SentPage(self.driver)
        homePage.click_sent()
        sentPage.check_pageOpen()
        sentPage.check_mail()


    def test_trash(self):
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_trash()

        trashPage = TrashPage(self.driver)
        trashPage.isTrashOpen()




