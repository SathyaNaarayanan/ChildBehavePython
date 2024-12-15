from behave import *

from ChildFrameworkMain.pages.LoginPage import LoginPage


@given(u'Launched LfynGo login page')
def launched_LfynGo_login_page(context):
    try:
        context.logger.info("Application launched")
        context.loginpage = LoginPage(context.driver)
        print("applicaiton launched")
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")



@when(u'I enter username and password')
def i_enter_username_and_password_like(context):
    try:
        context.logger.info("Entering username and password")
        for row in context.table:
            context.loginpage.enter_userName(row["email"])
            context.loginpage.enter_validPassword(row["password"])
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")


@when(u'I enter username as "{email}" and password as "{password}"')
def i_enter_username_and_password(context,email,password):
    try:
        context.logger.info("Entering username and password")
        context.loginpage.enter_userName(email)
        context.loginpage.enter_validPassword(password)
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")


@when(u'I enter username as "{email}" and invalid password as "{password}"')
def i_enter_username_and_invalid_password(context,email,password):
    try:
        context.logger.info("Entering username and invalid password")
        context.loginpage.enter_userName(email)
        context.loginpage.enter_inValidPassword(password)
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")


@when(u'I click on Submit button')
def step_impl(context):
    try:
        context.logger.info("click sunbmit button")
        context.homePage =  context.loginpage.click_submitButton()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")


@then(u'I navigated to LfnGo home page')
def step_impl(context):
    try:
        context.homePage.verify_dashboard_isDisplayed()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

@then(u'I verify error message')
def step_impl(context):
    try:
        context.loginpage.verify_errorMessage()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

