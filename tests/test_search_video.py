import time
import pytest
from pages.search_page import DuckDuckGoSearchPage
from pages.vid_page import DuckDuckGoVideoResultPage


def test_duckduckgo_video_search(browser, open_page, phrase):

    # click on the Video section
    vid_result = DuckDuckGoVideoResultPage(browser)
    vid_result.vid_search_result(phrase)
