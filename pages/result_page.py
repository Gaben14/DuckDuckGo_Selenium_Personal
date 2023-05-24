"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com)
page result call.
"""
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')
    MORE_RESULTS = (By.ID, 'more-results')
    AUTO_COMPLETE_CONT = (By.CSS_SELECTOR, 'div.search__autocomplete')
    AUTO_COMPLETE_RES = (By.CLASS_NAME, 'acp')

    # Initializer - using the browser fixture from the conftest.py
    def __init__(self, browser, phrase):
        self.browser = browser
        self.phrase = phrase

    # Interaction Methods:
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')

        assert self.phrase == value

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
        # Click inside the search input field - Here I'm already crossing against DRY, as I'm repeating the selector
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.click()

        # Select the 3rd result and click on it.
        third_result = self.browser.find_element(By.CSS_SELECTOR, 'div[data-index="3"]')
        third_result.click()
        # Go back to the page
        self.browser.back()

    # Handler function
    def search_result(self):
        # THEN the search result links equals to "panda"
        self.search_input_value()

        # AND click on the first result
        self.click_on_search_result()

        # AND verify (assert) that the autocomplete results contain the phrase
        assert self.verify_autocomplete()

        # AND select an autocomplete result
        self.select_autocomplete_selection()

        # AND click on the More Results button
        self.expand_more_result()
