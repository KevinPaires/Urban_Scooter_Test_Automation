import data

import helpers

import pages

from selenium import webdriver



class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')


    def test_set_route(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       urban_routes_page = pages.UrbanRoutesPage(self.driver)
       urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

       actual_value_from = urban_routes_page.get_value_in_from()
       expected_value_from = data.ADDRESS_FROM

       actual_value_to = urban_routes_page.get_value_in_to()
       expected_value_to = data.ADDRESS_TO

       assert actual_value_from in expected_value_from, f'Expected: {expected_value_from} Actual: {actual_value_from}'
       assert actual_value_to in expected_value_to, f'Expected: {expected_value_to} Actual: {actual_value_to}'

    def  test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.select_supportive_plan(data.ADDRESS_FROM, data.ADDRESS_TO)

        active_element = urban_routes_page.verify_supportive_text()
        assert "Supportive" in active_element, f'Expected: "Supportive" Actual: {active_element}'


    def test_fill_phone_number(self):

        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.fill_out_phone_number(data.ADDRESS_FROM, data.ADDRESS_TO, data.PHONE_NUMBER)

        actual_number = urban_routes_page.get_phone_number()
        expected_number = data.PHONE_NUMBER
        assert expected_number in actual_number, f'Expected: {expected_number} Actual: {actual_number}'

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.fill_out_credit_card_number(data.ADDRESS_FROM, data.ADDRESS_TO, data.CARD_NUMBER, data.CARD_CODE)

        actual_text = urban_routes_page.click_card_text()
        expected_text = "Card"
        assert expected_text in actual_text, f'Expected: {expected_text} Actual: {actual_text}'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.write_message_for_driver(data.ADDRESS_FROM, data.ADDRESS_TO, data.MESSAGE_FOR_DRIVER)

        actual_text = urban_routes_page.check_message_text()
        expected_text = data.MESSAGE_FOR_DRIVER
        assert actual_text in expected_text, f'Expected: {expected_text} Actual: {actual_text}'


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.check_blanket_and_handkerchiefs(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert urban_routes_page.is_slider_on(), f'Slider not enabled'

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.add_ice_cream(data.ADDRESS_FROM, data.ADDRESS_TO)

        actual_count = urban_routes_page.check_ice_cream_count()
        assert "2" in actual_count, f'Expected: {actual_count} Actual: {actual_count}'

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = pages.UrbanRoutesPage(self.driver)
        urban_routes_page.verify_modal_display(data.ADDRESS_FROM, data.ADDRESS_TO, data.PHONE_NUMBER, data.MESSAGE_FOR_DRIVER)

        assert urban_routes_page.modal_is_displayed(), f'false'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()