import pytest

from pageObjects.ComposePage import ComposePage
from pageObjects.HomePage import HomePage
from pageObjects.ImportantPage import ImportantPage
from pageObjects.LabelPage import LabelPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ScheduledPage import ScheduledPage
from pageObjects.SentPage import SentPage
from pageObjects.SpamPage import SpamPage
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


    @pytest.mark.checkmail
    def test_checkmail(self):
        homePage = HomePage(self.driver)
        sentPage = SentPage(self.driver)
        homePage.click_sent()
        sentPage.check_pageOpen()
        sentPage.check_mail()


    @pytest.mark.trash
    def test_trash(self):
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_trash()

        trashPage = TrashPage(self.driver)
        trashPage.isTrashOpen()
        trashPage.del_mail()


    @pytest.mark.label
    def test_label(self):
        homePage = HomePage(self.driver)
        homePage.click_add()

        labelPage = LabelPage(self.driver)
        labelPage.get_label()
        labelPage.create_label()

        homePage.check_label()


    @pytest.mark.checkLabel
    def test_checkLabel(self):
        homePage = HomePage(self.driver)
        homePage.check_label()


    @pytest.mark.spam
    def test_spam(self):
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_spam()

        spamPage = SpamPage(self.driver)
        spamPage.checkPage()


    @pytest.mark.important
    def test_important(self):
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_important()

        importantPage = ImportantPage(self.driver)
        importantPage.assert_page()


    @pytest.mark.scheduled
    def test_schelduled(self):
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_scheduled()

        scheduledPage = ScheduledPage(self.driver)
        scheduledPage.assert_page()









