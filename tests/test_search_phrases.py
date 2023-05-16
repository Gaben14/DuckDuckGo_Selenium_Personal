import time

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

    # WHEN the user searches for multiple "phrases" - Parametrize
    # search_page.search_multiple_phrases()

    # THEN the search result links equals to "panda"
    assert PHRASE == result_page.search_input_value()

    # AND click on the first result
    result_page.click_on_search_result()

    # AND verify (assert) that the autocomplete results contain the phrase
    assert result_page.verify_autocomplete()

    # AND select an autocomplete result
    result_page.select_autocomplete_selection()

    # AND click on the More Results button
    result_page.expand_more_result()

    # AND click on the Image section
    # result_page.img_search()

    # AND click on the Video section
    # result_page.vid_search()

    # AND click on the News section
    # result_page.news_search()

    # AND click on the Settings
    result_page.change_settings()
