from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from uitestcore.page import BasePage


class MotorwayResultsPage(BasePage):
    home_icon = PageElement(By.CSS_SELECTOR, 'a[aria-label="sell my car"]')
    model_info = PageElement(By.CSS_SELECTOR, '[data-cy="vehicleMakeAndModel"]')
    year = PageElement(By.CSS_SELECTOR, '[data-cy="vehicleSpecifics"] li:first-child')

    def is_results_page_displayed(self, reg):
        self.wait.for_page_to_load()
        value = f'[id="{reg}"]'
        selection = PageElement(By.CSS_SELECTOR, value)
        return self.interrogate.is_element_visible(selection)

    def click_home_icon(self):
        self.interact.click_element(self.home_icon)

    def fetch_model_info(self):
        self.wait.for_element_to_be_visible(self.model_info)
        return self.interrogate.get_text(self.model_info)

    def fetch_year(self):
        self.wait.for_element_to_be_visible(self.year)
        return self.interrogate.get_text(self.year)
