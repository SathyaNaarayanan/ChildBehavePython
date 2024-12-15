from selenium.webdriver.common.by import By

from ChildFrameworkMain.pages.HomePage import HomePage
from BaseBehavePython.pages.BasePage import *

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    userName = (By.XPATH, "//input[@name='email']")
    password = (By.NAME, "password")
    submit = (By.XPATH, "//button[text()='Submit']")
    errorMessage = (By.XPATH, "//div[@role='alert']//div[text()='Invalid username or password']")
    signInLabel = (By.XPATH, "//p[text()='Sign in']")


    def verify_signInPage(self):
        self.webElement_isDisplayed(self.signInLabel)

    def enter_userName(self, email):
        self.webElement_inputText(self.userName, email)

    def enter_validPassword(self,password):
        self.webElement_inputText(self.password, password)

    def enter_inValidPassword(self,password):
        self.webElement_inputText(self.password, password)

    def click_submitButton(self):
        self.webElement_click(self.submit)
        return HomePage(self.driver)

    def verify_errorMessage(self):
        self.webElement_isDisplayed(self.errorMessage)