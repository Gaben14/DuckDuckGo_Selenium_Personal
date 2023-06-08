from pages.old_files.img_page import DuckDuckGoImageResultPage


def test_duckduckgo_image_search(browser, open_page, phrase):

    # Initialize the Image Class
    img_result = DuckDuckGoImageResultPage(browser)

    # WHEN the user clicks on the images Tab, a: contains text "Images"
    img_click = img_result.when_img_tab_click()

    # THEN assert / verify if the images Tab has the is-active class
    img_result.then_assert_img_cls_list(img_click)

    # THEN assert / verify if the image title contains the Phrase
    img_result.then_assert_img_title(phrase)

    # AND close the image tab
    img_result.close()


