"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) video section
page result call.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

class DuckDuckGoNewsResultPage:

    # Locators:
    NEWS_TAB = (By.CSS_SELECTOR, 'a[data-zci-link="news"]')
    NEWS_8 = (By.CSS_SELECTOR, ':nth-child(8 of div.result--news)')

    # Initialize:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods:
    def news_search_result(self):
        # Click on the "News" Tab
        news_tab = self.browser.find_element(*self.NEWS_TAB)
        news_tab.click()

        # Open the 8th News Article
        news_8 = self.browser.find_element(*self.NEWS_8)
        news_8.click()

        # Go back to the NEWS page
        self.browser.back()

