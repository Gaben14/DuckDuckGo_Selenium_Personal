from pages.news_page import DuckDuckGoNewsResultPage


def test_duckduckgo_news_search(browser, open_page, phrase):

    # Initialize the News Class
    news_result = DuckDuckGoNewsResultPage(browser)

    # WHEN the user clicks on the news Tab
    cls_list = news_result.when_news_tab_click()

    # THEN assert / verify if the "News" Tab has the is-active class
    news_result.then_assert_news_cls_list(cls_list)

    # THEN assert / verify if the News title contains the Phrase
    news_result.then_assert_news_title(phrase)

    # THEN assert / verify if the News contains the Phrase (Open the page)
    news_result.then_assert_news_contains_phrase(phrase)
