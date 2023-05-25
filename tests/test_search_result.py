from pages.result_page import DuckDuckGoResultPage


def test_basic_duckduckgo_search(browser, open_page, phrase):
    # Open the Search Result age
    result_page = DuckDuckGoResultPage(browser)

    # THEN assert / verify that the user has entered the right value
    result_page.then_search_input_value(phrase)

    # AND click on the first search result
    result_page.click_on_search_result()

    # THEN assert / verify if the auto complete suggestions contain the phrase
    result_page.then_verify_autocomplete()

    # AND click on the Auto Complete Selection
    result_page.select_autocomplete_selection()

    # AND click on the More Results button
    result_page.expand_more_result()
