from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import localizadores as locz
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def __find_element(self, elm):
        return self.driver.find_element(*elm)

    def set_from(self, from_address):
        self.__find_element(locz.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.__find_element(locz.to_field).send_keys(to_address)

    def get_from(self):
        return self.__find_element(locz.from_field).get_property('value')

    def get_to(self):
        return self.__find_element(locz.to_field).get_property('value')

    def get_phone_in_field(self):
        return self.__find_element(locz.phone_field).text

    def get_card_option(self):
        return self.__find_element(locz.card_element_verify)

    def get_selected_tariff(self):
        return self.__find_element(locz.selected_tariff).get_attribute('innerHTML')

    def get_current_icecream_count_value(self):
        return self.__find_element(locz.icecream_counter).get_attribute('innerHTML')

    def get_comment_for_driver(self):
        return self.__find_element(locz.comment_to_driver).get_attribute('value')

    def is_blanket_checkbox_selected(self):
        return self.__find_element(locz.blanket_checkbox).is_selected()

    def get_order_screen_title(self):
        return self.__find_element(locz.order_wait_screen_title).get_attribute('innerText')

    def begin_cab_request(self):
        self.__find_element(locz.request_cab_button).click()

    def select_comfort_option(self):
        self.__find_element(locz.comfort_option).click()

    def enable_phone_input_dialog(self):
        self.__find_element(locz.phone_button).click()

    def enable_payment_input_dialog(self):
        self.__find_element(locz.payment_button).click()

    def enable_credit_card_input_dialog(self):
        self.__find_element(locz.creditcard_option).click()

    def insert_phone_to_dialog(self, phone_number):
        self.__find_element(locz.add_phone).send_keys(phone_number)

    def confirm_phone_click(self):
        self.__find_element(locz.confirm_phone).click()

    def insert_confirmation_code_to_dialog(self, confirmation_code):
        self.__find_element(locz.confirmation_code).send_keys(confirmation_code)

    def confirm_code_click(self):
        self.__find_element(locz.confirm_code_button).click()

    def insert_credit_card_number_to_field(self, cc_number):
        self.__find_element(locz.creditcard_number_field).send_keys(cc_number)

    def insert_credit_card_code_to_field(self, cc_code):
        self.__find_element(locz.creditcard_code_field).send_keys(cc_code)
        self.__find_element(locz.creditcard_code_field).send_keys(Keys.TAB)

    def click_confirm_credit_card(self):
        self.__find_element(locz.confirm_creditcard_button).click()

    def click_close_payment_modal(self):
        self.__find_element(locz.close_payment_modal_button).click()

    def insert_comment_for_driver(self, message_for_driver):
        self.__find_element(locz.comment_to_driver).send_keys(message_for_driver)

    def select_cloth_and_napkins(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(locz.blanket_slider))
        element.click()

    def is_blanket_checkbox_selected(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locz.blanket_checkbox))
        return element.is_selected()

    def fill_extra_options(self, message_for_driver):
        locz.wait_for_presence_input_field(self.driver, locz.reqs_form_open)
        self.insert_comment_for_driver(message_for_driver)
        self.select_cloth_and_napkins()
        self.select_add_icecream()
        self.select_add_icecream()

    def select_add_icecream(self):
        self.__find_element(locz.icecream_counter).click()

    def click_book_trip(self):
        self.__find_element(locz.book_cab_button).click()

    def set_route(self, address_from, address_to):
        locz.wait_for_presence_input_field(self.driver, locz.to_field)
        self.set_from(address_from)
        self.set_to(address_to)

    def request_comfort_cab(self):
        locz.wait_for_clickable_element(self.driver, locz.request_cab_button)
        self.begin_cab_request()
        locz.wait_for_clickable_element(self.driver, locz.comfort_option)
        self.select_comfort_option()

    def set_phone_number(self, phone_number):
        locz.wait_for_clickable_element(self.driver, locz.phone_button)
        self.enable_phone_input_dialog()
        locz.wait_for_presence_input_field(self.driver, locz.add_phone)
        self.insert_phone_to_dialog(phone_number)
        locz.wait_for_clickable_element(self.driver, locz.confirm_phone)
        self.confirm_phone_click()
        code = locz.retrieve_phone_code(self.driver)
        locz.wait_for_presence_input_field(self.driver, locz.confirmation_code)
        self.insert_confirmation_code_to_dialog(code)
        locz.wait_for_clickable_element(self.driver, locz.confirm_code_button)
        self.confirm_code_click()

    def set_credit_card_number(self, card_number, card_code):
        locz.wait_for_clickable_element(self.driver, locz.payment_button)
        self.enable_payment_input_dialog()
        locz.wait_for_clickable_element(self.driver, locz.creditcard_option)
        self.enable_credit_card_input_dialog()
        locz.wait_for_presence_input_field(self.driver, locz.creditcard_number_field)
        self.insert_credit_card_number_to_field(card_number)
        self.insert_credit_card_code_to_field(card_code)
        locz.wait_for_clickable_element(self.driver, locz.confirm_creditcard_button)
        self.click_confirm_credit_card()
        locz.wait_for_clickable_element(self.driver, locz.close_payment_modal_button)
        self.click_close_payment_modal()

    def book_trip(self):
        self.click_book_trip()
        locz.wait_for_visible_element(self.driver, locz.order_wait_screen)

    def wait_confirmation(self):
        locz.wait_for_visible_element(self.driver, locz.trip_confirmation, 5)
