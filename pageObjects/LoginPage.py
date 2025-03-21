from Locators.HomeLoc import HomeLoc
from Locators.LoginLoc import LoginLoc
from utilities.Wait import Wait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def getMail(self, email):
        mailbox = Wait.ec(self.driver, LoginLoc.emailid)
        mailbox.send_keys(email)

    def getPswd(self, password):
        pswdBox = Wait.ec(self.driver, LoginLoc.pswd)
        pswdBox.send_keys(password)

    def checkImg(self):
        img = Wait.pe(HomeLoc.gmailImg)
        assert img.is_displayed(), "Not logged in"

    def clickNext(self):
        next = Wait.ec(self.driver, LoginLoc.next)
        next.click()