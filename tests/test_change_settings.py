from pages.change_settings import DuckDuckGoSettings


def test_duckduckgo_news_search(browser, open_page):
    # Open the Settings menu
    change_settings = DuckDuckGoSettings(browser, "s", "b", "hu_HU", 'Austria')
