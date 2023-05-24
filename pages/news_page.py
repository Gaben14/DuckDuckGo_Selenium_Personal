"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) news section
page result call.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoNewsResultPage:
    # Locators:
    NEWS_TAB = (By.CSS_SELECTOR, 'a[data-zci-link="news"]')
    NEWS_8 = (By.CSS_SELECTOR, ':nth-child(8 of div.result--news)')
    NEWS_TITLE = (By.CSS_SELECTOR, ':nth-child(8 of div.result--news) > div.result__body > h2 > a.result__a')
    RESULT_PAGE_TITLE = (By.CSS_SELECTOR, '')

    # Initialize:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods:
    def news_search_result(self, phrase):
        # WHEN the user clicks on the "News" Tab
        news_tab = self.browser.find_element(*self.NEWS_TAB)
        news_tab.click()

        # THEN assert / verify if the "News" Tab has the is-active class
        cls_list = news_tab.get_attribute('class')
        assert 'is-active' in cls_list

        # AND open the 8th News Article
        news_8 = self.browser.find_element(*self.NEWS_8)
        news_8.click()

        # AND assert / verify if the News title contains the Phrase
        news_title = self.browser.find_element(*self.NEWS_TITLE).get_attribute('innerHTML').lower()
        assert phrase.lower() in news_title
        # AND assert / verify if the News contains the Phrase (Open the page) - Implement later
        assert phrase in self.browser.page_source
        # Go back to the NEWS page
        self.browser.back()



