from behave import *


@then(u'I click on profile menu')
def i_click_on_profile_menu(context):
    try:
        context.logger.info("Entered home screen - profile menu click")
        context.homePage.click_profileMenu()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

@when(u'I click on Logout option')
def i_click_on_Logout_option(context):
    try:
        context.logger.info("selecting logout option")
        context.homePage.click_logoutOption()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

@when(u'I acknowledge yes')
def i_acknowledge_yes(context):
    try:
        context.logger.info("Logout from application acknowledged YES")
        context.homePage.click_acknowledgeYes_Logout()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

@when(u'I acknowledge no')
def i_acknowledge_no(context):
    try:
        context.logger.info("Logout from application acknowledged NO")
        context.homePage.click_acknowledgeNo_Logout()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

@then(u'I navigated back to login screen')
def i_navigated_back_to_login_screen(context):
    try:
        context.logger.info("Navigate back to Login screen")
        context.loginpage.verify_signInPage()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

@then(u'I stay back to home screen')
def i_stay_back_to_home_screen(context):
    try:
        context.logger.info("Home screen")
        context.homePage.verify_dashboard_isDisplayed()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")

