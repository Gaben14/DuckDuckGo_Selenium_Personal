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
    VIDEO_2 = (By.CSS_SELECTOR, ':nth-child(2 of div.tile--vid)')
    VIDEO_TITLE = (By.CSS_SELECTOR, ':nth-child(2 of div.tile)  h6 > a')
    CLOSE_ICON = (By.CLASS_NAME, 'js-detail-close')

    # Initializer
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods
    def vid_search_result(self, phrase):
        # Click on the "Videos" link
        videos_tab = self.browser.find_element(*self.VIDEOS_TAB)
        videos_tab.send_keys(Keys.RETURN)

        # Check if the images Tab has the is-active class
        cls_list = videos_tab.get_attribute('class')
        assert 'is-active' in cls_list

        # Select the 2nd video class: tile--img
        video_2 = self.browser.find_element(*self.VIDEO_2)
        video_2.click()

        # Check if the video title contains the Phrase
        video_title = self.browser.find_element(*self.VIDEO_TITLE).get_attribute('innerHTML').lower()
        assert phrase.lower() in video_title

        # Click on the X icon - class: js-detail-close or detail__close
        close_icon = self.browser.find_element(*self.CLOSE_ICON)
        # Sometimes there are two occurrences of the close icon when using videos, the second 1 is the one we need.
        close_icon.click()

