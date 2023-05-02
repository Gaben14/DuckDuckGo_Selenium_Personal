from pages.search_page import DuckDuckGoSearchPage
from pages.result_page import DuckDuckGoResultPage
import pytest


def test_basic_duckduckgo_search(browser):
    # Class initiation
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # PHRASES to search for - Update to parametrize later!
    PHRASE = 'panda'

    # GIVEN The DuckDuckGo page is displayed
    search_page.load()

    # WHEN the user searches for a single "phrase"
    search_page.search_single_phrase(PHRASE)

    # WHEN the user searches for multiple "phrases"
    # search_page.search_multiple_phrases()

    # THEN the search result links equals to "panda"
    assert PHRASE == result_page.search_input_value()

    # AND click on the first result
    result_page.click_on_search_result()

    # AND click on the More Results button
    result_page.expand_more_result()


