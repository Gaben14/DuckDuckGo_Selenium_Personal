from pages.result_page import DuckDuckGoResultPage
import pytest


def test_basic_duckduckgo_search(browser, open_page, phrase):
    # Open the Search Result age
    result_page = DuckDuckGoResultPage(browser, phrase)
    result_page.search_result()
