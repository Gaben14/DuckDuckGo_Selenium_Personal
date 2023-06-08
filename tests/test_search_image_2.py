from pages.search_tab import DuckDuckGoSearchTab


def test_duckduckgo_image_search(browser, open_page, phrase):
    # Initialize the Image Class
    img_result = DuckDuckGoSearchTab(browser, 'images')

    # WHEN the user clicks on the images Tab, a: contains text "Images"
    img_click = img_result.when_tab_click()

    # THEN assert / verify if the images Tab has the is-active class
    img_result.then_assert_tab_cls_list(img_click)

    # THEN assert / verify if the image title contains the Phrase
    img_result.then_assert_item_title(phrase, ':nth-child(4 of div.tile) > a > .tile--img__title')

    # THEN assert / verify if
    # img_result.then_assert_child_contains_phrase(phrase, 4)

    # AND close the image tab
    # img_result.close()
