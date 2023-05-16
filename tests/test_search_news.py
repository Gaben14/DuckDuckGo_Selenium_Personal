import pytest
from pages.search_page import DuckDuckGoSearchPage
from pages.news_page import DuckDuckGoNewsResultPage


def test_duckduckgo_news_search(browser):
    # Todo - Class initiation until the search should be moved maybe to the conftest.py file?
    # Class initiation
    search_page = DuckDuckGoSearchPage(browser)

    # PHRASES to search for - Update to parametrize later!
    PHRASE = 'panda'

    # GIVEN The DuckDuckGo page is displayed
    search_page.load()

    # WHEN the user searches for a single "phrase"
    search_page.search_single_phrase(PHRASE)

    # click on the News section
    news_result = DuckDuckGoNewsResultPage(browser)
    news_result.news_search_result(PHRASE)
