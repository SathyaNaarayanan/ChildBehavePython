from sys import exception
import allure
from allure_commons.types import AttachmentType
from cffi.backend_ctypes import xrange
from selenium.webdriver.remote.webdriver import WebDriver
from ChildFrameworkMain.utilities import configReader
from BaseBehavePython.features.environment import driver_close, logger_Predefined, driver_initialization, launchApplication
from BaseBehavePython.features.environment import getApplicationURL, getBrowser

_configFilePath = "ChildFrameworkMain/configurations/config.ini"
#hooks
def before_all(context):
    context.logger = logger_Predefined("ChildFrameworkMain", "LYFnGO-Logger")

def before_scenario(context, scenario):
    try:
        context.driver: WebDriver = driver_initialization(getBrowser(_configFilePath))
        context.driver.maximize_window()
        launchApplication(context.driver, getApplicationURL(_configFilePath))
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

def getApplicationURL(filePath):
    return configReader.read_configuration(filePath, "basic info", "url")

def getBrowser(filePath):
    return configReader.read_configuration(filePath,"basic info", "browser").lower()



