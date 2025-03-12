from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from uitestcore.page import BasePage


class MotorwayHomePage(BasePage):
    reg_input_textbox = PageElement(By.ID, "vrm-input")
    submit_button = PageElement(By.CSS_SELECTOR, '#main button[type="submit"]')

    def enter_reg(self, reg):
        self.wait.for_element_to_be_visible(self.reg_input_textbox)
        self.interact.enter_text(self.reg_input_textbox, reg)

    def click_submit_button(self):
        self.interact.click_element(self.submit_button)
