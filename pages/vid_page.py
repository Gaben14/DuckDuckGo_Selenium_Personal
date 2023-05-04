"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) video section
page result call.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoVideoResultPage:
    # Locators
    VIDEOS_TAB = (By.CSS_SELECTOR, 'a[data-zci-link="videos"]')
    VIDEO_2 = (By.CSS_SELECTOR, ':nth-child(4 of div.tile--vid)')
    CLOSE_ICON = (By.CLASS_NAME, 'js-detail-close')

    # Initializer
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods
    def vid_search_result(self):
        # Click on the "Videos" link
        videos_tab = self.browser.find_element(*self.VIDEOS_TAB)
        videos_tab.send_keys(Keys.RETURN)

        # Select the 2nd video class: tile--img
        video_2 = self.browser.find_element(*self.VIDEO_2)
        video_2.click()

        # Click on the X icon - class: js-detail-close or detail__close
        close_icon = self.browser.find_elements(*self.CLOSE_ICON)
        # There are two occurrences of the close icon when using videos, the second 1 is the one we need.
        close_icon[1].click()
        # close_icon.click()
        # close_icon.send_keys(Keys.RETURN)
