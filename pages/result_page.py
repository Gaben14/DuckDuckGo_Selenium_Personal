"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com)
page result call.
"""
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.img_page import DuckDuckGoImageResultPage
from pages.vid_page import DuckDuckGoVideoResultPage
from pages.news_page import DuckDuckGoNewsResultPage
from pages.change_settings import DuckDuckGoSettings


class DuckDuckGoResultPage:
    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')
    MORE_RESULTS = (By.LINK_TEXT, 'More Results')
    AUTO_COMPLETE_CONT = (By.CSS_SELECTOR, 'div.search__autocomplete')
    AUTO_COMPLETE_RES = (By.CLASS_NAME, 'acp')

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
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)[0]
        search_results.click()

        # Go back to the result page
        self.browser.back()

    def expand_more_result(self):
        # Click on the More Results button
        more_results_btn = self.browser.find_element(*self.MORE_RESULTS)
        more_results_btn.click()

    def verify_autocomplete(self):
        # Create the selector for the container of the autocomplete div
        auto_complete_cont = self.browser.find_element(*self.AUTO_COMPLETE_CONT)
        # Click inside the search input field - Here I'm already crossing against DRY, as I'm repeating the selector
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.click()
        search_input_val = self.browser.find_element(*self.SEARCH_INPUT).get_attribute("innerHTML")
        # Search for all the spans with the class 't-normal'
        autocomp_results = self.browser.find_elements(*self.AUTO_COMPLETE_RES)
        # Check if the search_input_value can be found inside the spans

        for result in autocomp_results:
            # assert self.search_input_value() == result.get_attribute('innerHTML')
            if search_input_val in result.get_attribute("innerHTML"):
                return True
            else:
                return False

    def select_autocomplete_selection(self):
        # Create the selector for the container of the autocomplete div
        auto_complete_cont = self.browser.find_element(*self.AUTO_COMPLETE_CONT)
        # Click inside the search input field - Here I'm already crossing against DRY, as I'm repeating the selector
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.click()

        # Select the 3rd result and click on it.
        third_result = self.browser.find_element(By.CSS_SELECTOR, 'div[data-index="3"]')
        third_result.click()
        # Go back to the page
        self.browser.back()

    def img_search(self):
        img_result = DuckDuckGoImageResultPage(self.browser)
        img_result.img_search_result()

    def vid_search(self):
        vid_result = DuckDuckGoVideoResultPage(self.browser)
        vid_result.vid_search_result()

    def news_search(self):
        news_result = DuckDuckGoNewsResultPage(self.browser)
        news_result.news_search_result()

    def change_settings(self):
        change_duck_settings = DuckDuckGoSettings(self.browser)
        change_duck_settings.duck_settings("s", "b", "hu_HU", 'Austria')
