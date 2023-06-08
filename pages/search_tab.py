"""
This file / class will be created to use OOP for the multiple search options
One class which will do the main functionality, which all child classes will have.

If a child class needs extra functionality it will extend the parent class.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoSearchTab:
    # Locators
    CLOSE_ICON = (By.CLASS_NAME, 'detail__close')
    VIDEO_TITLE = (By.CSS_SELECTOR, ':nth-child(2 of div.tile)  h6 > a')
    # Constructor
    def __init__(self, browser: WebDriver, tab_type):
        self.browser = browser
        self.tab_type = tab_type

    def when_tab_click(self):
        browser_tab = self.browser.find_element(By.CSS_SELECTOR, f'a[data-zci-link="{self.tab_type}"]')
        browser_tab.send_keys(Keys.RETURN)

        browser_tab_cls_list = browser_tab.get_attribute('class')
        return browser_tab_cls_list

    def then_assert_tab_cls_list(self, cls_list):
        print(cls_list)
        assert 'is-active' in cls_list

    def then_assert_item_title(self, phrase, selector,):
        # AND assert / verify if the (in your Tab) Item title contains the Phrase
        item_title = self.browser.find_element(By.CSS_SELECTOR, selector).get_attribute(
            'innerHTML').lower()
        assert phrase.lower() in item_title

    # This method should only be executed for News
    def then_assert_child_contains_phrase(self, phrase, item_num):
        # AND open the ..th item of the specified Tab
        child_item = self.browser.find_element(By.CSS_SELECTOR, f':nth-child({item_num} of div.tile--vid)')
        child_item.click()

        if self.tab_type == 'news':
            # AND assert / verify if the News contains the Phrase (Open the page)
            assert phrase in self.browser.page_source
            # Go back to the NEWS page
            self.browser.back()
        else:
            child_title = child_item.get_attribute('innerHTML').lower()
            assert phrase.lower() in child_title

    # AND the user clicks on the X icon
    def close(self):
        # AND the user clicks on the X icon - class: js-detail-close or detail__close
        close_icon = self.browser.find_element(*self.CLOSE_ICON)
        # Sometimes there are two occurrences of the close icon when using videos, the second 1 is the one we need.
        close_icon.click()
