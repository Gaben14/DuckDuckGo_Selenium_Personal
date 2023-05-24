"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com)
page call, and entering a search entry inside the search input field.
"""
from selenium.webdriver.common.by import By
import requests


class DuckDuckGoSearchPage:
    # Class Variables
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button[aria-label="Search"]')

    # Constructor
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        # GIVEN the user opens the web-page.
        self.browser.get(self.URL)

        # THEN Verify / Assert if the response code is 200 for loading the page
        response = requests.get(self.URL)
        assert response.status_code == 200

    # Single Phrase
    def search_single_phrase(self, phrase):
        # WHEN the user clicks on the Search bar, clear all previously entered values and enter the user's entry
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(phrase)
        # THEN assert / verify that the phrase and the value of the input is the same.
        search_btn = self.browser.find_element(*self.SEARCH_BTN)
        search_btn.click()
