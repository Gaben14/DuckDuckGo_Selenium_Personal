"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com)
page call, and entering a search entry inside the search input field.
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


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
        self.browser.get(self.URL)
        # TODO Assert if the response code is 200 for loading the page
        # print(self.browser.get(self.URL))

    # Single Phrase
    def search_single_phrase(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(phrase)
        # Assert that phrase and the value of the input is the same.
        search_btn = self.browser.find_element(*self.SEARCH_BTN)
        search_btn.click()

    # Multiple phrases
    phrases = ['panda', 'snake', 'dog']

    @pytest.mark.parametrize('phrase', phrases)
    def search_multiple_phrases(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_btn = self.browser.find_element(*self.SEARCH_BTN)
        search_btn.click()
