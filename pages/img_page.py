"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) images section
page result call.
"""
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
        # WHEN the user clicks on the images Tab, a: contains text "Images"
        images_tab = self.browser.find_element(*self.IMAGES_TAB)
        images_tab.send_keys(Keys.RETURN)

        # THEN check / verify if the images Tab has the is-active class
        cls_list = images_tab.get_attribute('class')
        assert 'is-active' in cls_list

        # AND select the 4th image class: tile--img
        image_4 = self.browser.find_element(*self.IMAGE_4)
        image_4.click()

        # AND check / verify if the image title contains the Phrase
        img_title = self.browser.find_element(*self.IMAGE_TITLE).get_attribute('innerHTML').lower()
        assert phrase.lower() in img_title

        # AND the user clicks on the X icon
        close_icon = self.browser.find_element(*self.CLOSE_ICON)
        close_icon.click()
