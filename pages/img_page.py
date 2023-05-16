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
    IMAGE_TITLE = (By.CSS_SELECTOR, ':nth-child(4 of div.tile) > a > .tile--img__title')
    CLOSE_ICON = (By.CLASS_NAME, 'detail__close')

    # Initializer
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods:
    def img_search_result(self, phrase):
        # Click on the images Tab, a: contains text "Images"
        images_tab = self.browser.find_element(*self.IMAGES_TAB)
        images_tab.send_keys(Keys.RETURN)

        # Check if the images Tab has the is-active class
        cls_list = images_tab.get_attribute('class')
        assert 'is-active' in cls_list

        # Select the 4th image class: tile--img
        image_4 = self.browser.find_element(*self.IMAGE_4)
        image_4.click()

        # Check if the image title contains the Phrase
        img_title = self.browser.find_element(*self.IMAGE_TITLE).get_attribute('innerHTML').lower()
        assert phrase.lower() in img_title

        # Click on the X icon - class: js-detail-close or detail__close
        close_icon = self.browser.find_element(*self.CLOSE_ICON)
        close_icon.click()
