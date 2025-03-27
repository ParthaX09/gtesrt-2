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
        log = self.get_logger()
        loginPage = LoginPage(self.driver)
        loginPage.checkImg()
        log.info("Successful login")

    @pytest.mark.compose
    def test_compose(self, get_data):
        log = self.get_logger()
        email = get_data
        composePage = ComposePage(self.driver)
        composePage.clickCompose()
        composePage.get_to(email)
        composePage.get_sub()
        composePage.get_desc()
        composePage.click_send()
        composePage.check_sent()
        log.info("Successful mail sent")



    @pytest.mark.checkmail
    def test_checkmail(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        sentPage = SentPage(self.driver)
        homePage.click_sent()
        sentPage.check_pageOpen()
        sentPage.check_mail()
        log.info("Mail checked")



    @pytest.mark.trash
    def test_trash(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_trash()
        log.info("Moved to trash page")

        trashPage = TrashPage(self.driver)
        trashPage.isTrashOpen()
        trashPage.del_mail()
        log.info("Deleted mail from trash")



    @pytest.mark.label
    def test_label(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.click_add()

        labelPage = LabelPage(self.driver)
        labelPage.get_label()
        labelPage.create_label()
        log.info("Label created")


    @pytest.mark.checkLabel
    def test_checkLabel(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.check_label()
        log.info("Label checked")


    @pytest.mark.spam
    def test_spam(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_spam()
        log.info("Moved to spam page")

        spamPage = SpamPage(self.driver)
        spamPage.checkPage()
        log.info("Spam page checked")


    @pytest.mark.important
    def test_important(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_important()
        log.info("Moved to important page")

        importantPage = ImportantPage(self.driver)
        importantPage.assert_page()
        log.info("Checked important page")


    @pytest.mark.scheduled
    def test_schelduled(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.click_more()
        homePage.click_scheduled()
        log.info("Scheduled opened")

        scheduledPage = ScheduledPage(self.driver)
        scheduledPage.assert_page()
        log.info("Scheduled checked")