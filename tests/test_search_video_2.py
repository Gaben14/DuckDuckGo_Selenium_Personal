from pages.search_tab import DuckDuckGoSearchTab


def test_duckduckgo_image_search(browser, open_page, phrase):
    # Initialize the Video Class
    vid_result = DuckDuckGoSearchTab(browser, 'videos')

    # WHEN the user clicks on the Video Tab, a: contains text "Images"
    vid_click = vid_result.when_tab_click()

    # THEN assert / verify if the Video Tab has the is-active class
    vid_result.then_assert_tab_cls_list(vid_click)

    # THEN assert / verify if the Video title contains the Phrase
    vid_result.then_assert_item_title(phrase, ':nth-child(2 of div.tile)  h6 > a')

    # THEN assert / verify if
    vid_result.then_assert_child_contains_phrase(phrase, 2)
    # AND close the image tab
    vid_result.close()
