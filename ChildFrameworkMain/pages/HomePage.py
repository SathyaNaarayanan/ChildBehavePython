import time
from selenium.webdriver.common.by import By
from BaseBehavePython.pages.BasePage import *

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    dashboard = (By.XPATH, "//h6[text()='Dashboard']")
    profile = (By.XPATH, "//button/div/p[text()='Owner']")
    logout = (By.XPATH, "//span[text()='Logout']")
    logOutAcknowledgeYes = (By.XPATH, "//button/div[text()='Yes']")
    logOutAcknowledgeNo = (By.XPATH, "//button/div[text()='No']")

    def click_acknowledgeNo_Logout(self):
        time.sleep(1) #exception cases - as application is not consistent at this point
        self.webElement_click(self.logOutAcknowledgeNo)

    def click_acknowledgeYes_Logout(self):
        time.sleep(1) #exception cases - as application not consistent at this point
        self.webElement_click(self.logOutAcknowledgeYes)

    def click_logoutOption(self):
        time.sleep(1) #exception cases - as application not consistent at this point
        self.webElement_click(self.logout)

    def click_profileMenu(self):
        self.webElement_click(self.profile)

    def verify_dashboard_isDisplayed(self):
        time.sleep(3)
        self.webElement_isDisplayed(self.dashboard)
        label = self.webElement_getText(self.dashboard)
        assert label == 'Dashboard'
