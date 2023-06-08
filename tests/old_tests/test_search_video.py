from pages.old_files.vid_page import DuckDuckGoVideoResultPage


def test_duckduckgo_video_search(browser, open_page, phrase):

    # Initialize the Video Class
    vid_result = DuckDuckGoVideoResultPage(browser)

    # WHEN the user clicks on the "Videos" link
    vid_click = vid_result.when_vid_tab_click()

    # THEN assert / verify if the images Tab has the is-active class
    vid_result.then_assert_vid_cls_list(vid_click)

    # THEN assert / verify if the video title contains the Phrase
    vid_result.then_assert_vid_title(phrase)

    # AND close the video tab
    vid_result.close()
    """
    Refactor the test case to have the GIVEN - WHEN - THEN structure here,
    instead in the handler function
    function name for WHEN - THEN should include these words. (when_clicking... or then_)
    vid_result.then_ or vid_result.when_
    """
