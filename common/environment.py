import json
import logging
import os
from behave.model_core import Status
from uitestcore.utilities import logger_handler
from uitestcore.utilities.browser_handler import BrowserHandler

"""
Description:    This class is executed before any Behave code, loads the browser and reads and sets the configuration.
                It also checks to see if there are flags provided as a command line parameter to overwrite the config.
"""


def before_all(context):
    """
    This function is executed before any Behave code
    :param context: the test context instance
    """
    # Read the config file and set the values, but the Command Line may override
    test_config_file = os.environ['CONFIG_FILE'] if 'TEST_CONFIG_FILE' in os.environ else 'config/CONFIG_FILE.json'
    with open(test_config_file) as data_file:
        config = json.load(data_file)
        context.browser_name = config['browser']
        context.browser_options = config['browser_options']
        context.maximize_browser = config['maximize_browser_flag']
        context.explicit_wait = config['explicit_wait']
        context.url = config['base_url']


def before_scenario(context, scenario):
    """
    This function is executed before each scenario
    :param context: the test context instance
    :param scenario: the test scenario instance
    """
    context.logger.log(20, "-----------------------------------------------------------------")
    context.logger.log(20, "STARTING SCENARIO: " + scenario.name)
    context.logger.log(20, "-----------------------------------------------------------------")

    BrowserHandler.prepare_browser(context)


def after_scenario(context, scenario):
    """
    This function is executed after each scenario
    :param context: the test context instance
    :param scenario: the test scenario instance
    """
    context.logger.log(20, "-----------------------------------------------------------------")
    context.logger.log(20, f"SCENARIO ENDED: '{scenario.name}' STATUS: {scenario.status.name}")
    context.logger.log(20, "-----------------------------------------------------------------")

    context.browser.quit()
