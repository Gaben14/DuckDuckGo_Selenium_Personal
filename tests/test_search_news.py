from pages.news_page import DuckDuckGoNewsResultPage


def test_duckduckgo_news_search(browser, open_page, phrase):

    # Open the News section
    news_result = DuckDuckGoNewsResultPage(browser, phrase)

