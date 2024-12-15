from sys import exception
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from ChildFrameworkMain.utilities import configReader
from BaseBehavePython.features.environment import driver_close, logger_Predefined, driver_initialization, launchApplication
from BaseBehavePython.utilities.DriverManager import *

#hooks
def before_all(context):
    context.logger = logger_Predefined("ChildFrameworkMain", "LYFnGO-Logger")

def before_scenario(context, scenario):
    try:
        context.driver = driver_initialization(getBrowser())
        context.driver: WebDriver = DriverManager.get_driverInstance().get_driver()
        context.driver.maximize_window()
        launchApplication(context.driver, getApplicationURL())
    except Exception as e:
        context.logger.error(f"ERROR : {str(e)}")
        raise

def before_step(context, step):
    try:
        context.logger.info(f"function step started: {step.name}")
    except exception as e:
        context.logger.error(f"ERROR : {str(e)}")
        raise


def after_step(context, step):
    try:
        if step.status == "passed":
            context.logger.info(f"function step passed: {step.name}")
        elif step.status == "failed":
            context.logger.info(f"function step failed: {step.name}")

        if step.status == 'passed':
            allure.attach(context.driver.get_screenshot_as_png()
                          , name="passed_screenshot"
                          , attachment_type=AttachmentType.PNG)
        if step.status == 'failed':
            allure.attach(context.driver.get_screenshot_as_png()
                          , name="failed_screenshot"
                          , attachment_type=AttachmentType.PNG)
    except Exception as e:
        context.logger.error(f"ERROR : {str(e)}")
        raise

def after_scenario(context, scenario):
    driver_close(context.driver)

def getApplicationURL():
    return configReader.read_configuration("basic info", "url")

def getBrowser():
    return configReader.read_configuration("basic info", "browser").lower()




