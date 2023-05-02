"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com)
page result call.
"""
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoResultPage:
    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')
    MORE_RESULTS = (By.LINK_TEXT, 'More Results')

    # Initializer - using the browser fixture from the conftest.py
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods:
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def click_on_search_result(self):
        # Select the first result, click on it
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)[0].click()
        # Go back to the result page
        self.browser.back()

    def expand_more_result(self):
        # Click on the More Results button
        more_results_btn = self.browser.find_element(*self.MORE_RESULTS).click()

