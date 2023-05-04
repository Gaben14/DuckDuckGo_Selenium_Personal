"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) images section
page result call.

TODO - Should I convert this class to a child class?
(Parent should be the DuckDuckGoResultPage?)
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoImageResultPage:
    # Locators
    IMAGES_TAB = (By.CSS_SELECTOR, 'a[data-zci-link="images"]')
    IMAGE_4 = (By.CSS_SELECTOR, ':nth-child(4 of div.tile)')
    CLOSE_ICON = (By.CLASS_NAME, 'detail__close')

    # Initializer
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods:
    def img_search_result(self):
        # Click on the images Tab, a: contains text "Images"
        images_tab = self.browser.find_element(*self.IMAGES_TAB)
        images_tab.send_keys(Keys.RETURN)

        # Select the 4th image class: tile--img
        image_4 = self.browser.find_element(*self.IMAGE_4)
        # Click on the 4th image
        image_4.click()

        # Click on the X icon - class: js-detail-close or detail__close
        close_icon = self.browser.find_element(*self.CLOSE_ICON)
        close_icon.click()
