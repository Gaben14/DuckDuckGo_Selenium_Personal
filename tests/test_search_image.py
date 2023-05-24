from pages.img_page import DuckDuckGoImageResultPage


def test_duckduckgo_image_search(browser, open_page, phrase):

    # Open the Image section
    img_result = DuckDuckGoImageResultPage(browser)
    img_result.img_search_result(phrase)


