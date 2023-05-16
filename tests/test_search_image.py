import time

from pages.search_page import DuckDuckGoSearchPage
from pages.result_page import DuckDuckGoResultPage
from pages.result_page import DuckDuckGoImageResultPage
import pytest


def test_duckduckgo_image_search(browser):
    # click on the Image section
    img_result = DuckDuckGoImageResultPage(browser)
    img_result.img_search_result()

    # - Assert / Verify if the Images tab is selected / currently active
    # Check if the tab has the is-active class
    # assert
