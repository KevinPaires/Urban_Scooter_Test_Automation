
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import helpers

class UrbanRoutesPage:
    # supportive option locators
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    LOCATE_TAXI_ICON =  (By.XPATH, '//img[contains(@src, "taxi-active") and contains(@class, "type-icon")]')
    LOCATE_TAXI_BUTTON = (By.XPATH, '//button[@class="button round"]' )
    LOCATE_SUPPORTIVE_ICON = (By.XPATH, '//img[@alt="Supportive"]')
    # Phone number locators
    LOCATE_PHONE_NUMBER = (By.XPATH, '//div[@class="np-text" and text()="Phone number"]')
    LOCATE_ENTER_PHONE_NUMBER = (By.ID, 'phone')
    LOCATE_PHONE_NUMBER_BUTTON = (By.XPATH, '//button[@class="button full"]')
    # PHONE_CODE = (By.ID, 'code')
    ENTER_CARD_CODE = (By.XPATH, '//label[text()="Enter the code]')
    CONFIRM_PHONE_CODE = (By.XPATH, '//button[@type="submit" and normalize-space()="Confirm"]')
    SUPPORTIVE_TEXT_LOCATOR = (By.CSS_SELECTOR, '.tcard.active')
    # CC LOCATORS
    LOCATE_PAYMENT_METHOD = (By.XPATH, '//div[@class="pp-button filled"]')
    ADD_CREDIT_CARD = (By.XPATH, '//img[contains(@src, "plus") and contains(@class, "pp-plus")]')
    ENTER_CREDIT_CARD = (By.ID, "number")
    TYPE_CREDIT_CARD_CODE = (By.NAME, 'code')
    LOCATE_LINK_BUTTON = (By.XPATH, '//button[normalize-space()="Link"]')
    LOCATE_CARD_TEXT = (By.XPATH, '//div[@class="pp-value-text"]')
    DRIVER_MESSAGE = (By.ID, 'comment')
    # slider locators
    LOCATE_SLIDER = (By.XPATH, '//span[@class="slider round"]')
    LOCATE_CHECKBOX = (By.XPATH, '//input[@class="switch-input"]')
    # ice cream locators
    LOCATE_ADD_ICE_CREAM = (By.CLASS_NAME, 'counter-plus')
    LOCATE_ICE_CREAM_COUNT = (By.CLASS_NAME, 'counter-value')
    # modal locators
    LOCATE_ORDER_BUTTON = (By.XPATH, '//button[@class="smart-button"]')
    LOCATE_MODAL = (By.XPATH, '//div[@class="order-subbody"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_value_in_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def get_value_in_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    def click_custom_option_button(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_taxi_icon(self):
        self.driver.find_element(*self.LOCATE_TAXI_ICON).click()

    def click_taxi_button(self):
        self.driver.find_element(*self.LOCATE_TAXI_BUTTON).click()

    def click_supportive_icon(self):
        self.driver.find_element(*self.LOCATE_SUPPORTIVE_ICON).click()

    def verify_supportive_text(self):
        return self.driver.find_element(*self.SUPPORTIVE_TEXT_LOCATOR).text

    def click_enter_phone_number(self):
        self.driver.find_element(*self.LOCATE_PHONE_NUMBER).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.LOCATE_ENTER_PHONE_NUMBER).send_keys(phone_number)

    def click_add_phone_number(self):
        self.driver.find_element(*self.LOCATE_PHONE_NUMBER_BUTTON).click()

    def click_phone_code(self, code):
        self.driver.find_element(*self.PHONE_CODE).send_keys(code)

    def get_phone_number(self):
        return self.driver.find_element(*self.LOCATE_ENTER_PHONE_NUMBER).get_attribute("value")

    def enter_code_in_code_field(self):
        self.driver.find_element(*self.ENTER_CARD_CODE).click()

    def click_payment_method(self):
        self.driver.find_element(*self.LOCATE_PAYMENT_METHOD).click()

    def click_add_credit_card(self):
        self.driver.find_element(*self.ADD_CREDIT_CARD).click()

    def click_enter_credit_card(self):
        self.driver.find_element(*self.ENTER_CREDIT_CARD).click()

    def enter_credit_card(self, credit_card):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ENTER_CREDIT_CARD)
        )
        field.clear()
        field.send_keys(credit_card)

    def enter_credit_card_code(self, code):
        cvv_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TYPE_CREDIT_CARD_CODE)
        )
        cvv_field.clear()
        cvv_field.send_keys(code)
        cvv_field.send_keys(Keys.TAB)


    def click_link_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATE_LINK_BUTTON)
        )
        button.click()
    def click_card_text(self):
        return self.driver.find_element(*self.LOCATE_CARD_TEXT).text

    def comment_for_driver(self, message):
        self.driver.find_element(*self.DRIVER_MESSAGE).send_keys(message)

    def check_message_text(self):
        return self.driver.find_element(*self.DRIVER_MESSAGE).text

    def click_slider(self):
        slider = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATE_SLIDER)
        )
        slider.click()

    def is_slider_on(self):

        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATE_CHECKBOX)
        )
        return checkbox.get_property("checked")

    def click_add_ice_cream(self):
        for i in range (2):
            self.driver.find_element(*self.LOCATE_ADD_ICE_CREAM).click()


    def check_ice_cream_count(self):
        return self.driver.find_element(*self.LOCATE_ICE_CREAM_COUNT).text

    def click_order_button(self):
        self.driver.find_element(*self.LOCATE_ORDER_BUTTON).click()

    def modal_is_displayed(self):
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATE_MODAL)
        )
        return modal.is_displayed()

    def click_confirm_code(self):
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CONFIRM_PHONE_CODE)
        )
        modal.click()



    def select_supportive_plan(self, from_text, to_text):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        time.sleep(5)

    def fill_out_phone_number(self, from_text, to_text, phone_number):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        self.click_enter_phone_number()
        self.enter_phone_number(phone_number)
        self.click_add_phone_number()
        code = helpers.retrieve_phone_code(self.driver)
        self.click_phone_code(code)
        time.sleep(5)
        self.click_confirm_code()

    def fill_out_credit_card_number(self, from_text, to_text, credit_card, code):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        self.click_payment_method()
        time.sleep(5)
        self.click_add_credit_card()
        time.sleep(10)
        self.enter_credit_card(credit_card)
        self.enter_credit_card_code(code)
        self.click_link_button()
        time.sleep(5)


    def write_message_for_driver(self, from_text, to_text, message):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        time.sleep(5)
        self.comment_for_driver(message)

    def check_blanket_and_handkerchiefs(self, from_text, to_text):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        self.click_slider()
        time.sleep(5)

    def add_ice_cream(self,from_text, to_text):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        self.click_add_ice_cream()
        time.sleep(5)

    def verify_modal_display(self, from_text, to_text, phone_number, message):
        self.driver.implicitly_wait(5)
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option_button()
        self.click_taxi_icon()
        self.click_taxi_button()
        self.click_supportive_icon()
        self.click_enter_phone_number()
        self.enter_phone_number(phone_number)
        self.click_add_phone_number()
        code = helpers.retrieve_phone_code(self.driver)
        self.click_phone_code(code)
        time.sleep(5)
        self.click_confirm_code()
        time.sleep(5)
        self.comment_for_driver(message)
        self.click_order_button()



















