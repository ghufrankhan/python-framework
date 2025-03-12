from behave import Step
from pages.motorway_home_page import MotorwayHomePage
from pages.motorway_results_page import MotorwayResultsPage


@Step("I navigate to the motorway website")
def go_to_motorway_website(context):
    context.home_page = MotorwayHomePage(context.browser, context.logger, context.explicit_wait)
    context.results_page = MotorwayResultsPage(context.browser, context.logger, context.explicit_wait)

    context.home_page.interact.open_url(context.url)


@Step("I enter each of the extracted registration numbers and populate the results data")
def enter_reg_and_populate(context):
    context.car_details = []

    for reg in context.registration_plates:
        # Enter reg nums and click submit
        context.home_page.enter_reg(reg)
        context.home_page.click_submit_button()

        # Wait for results page and fetch data
        context.results_page.is_results_page_displayed(reg)
        model_info = context.results_page.fetch_model_info()
        year = context.results_page.fetch_year()

        # Append details to list and sacve to context
        context.car_details.append(f"{reg},{model_info},{year}")

        # Go to home page to start over
        context.results_page.click_home_icon()
