from pages.change_settings import DuckDuckGoSettings


def test_duckduckgo_news_search(browser, open_page):
    # Open the Settings menu
    change_settings = DuckDuckGoSettings(browser)
    # change_settings.change_duck_settings("s", "b", "hu_HU", 'Austria')

    change_settings.open_menu()
    # WHEN the user clicks on the Dark Mode button (Change to Dark Mode)
    dm_cls_list = change_settings.when_dark_mode_click()

    # THEN assert / verify if the page has changed to Dark Mode (has the is-checked class)
    change_settings.then_assert_dark_mode_cls_list(dm_cls_list)

    # WHEN the user clicks on the 'New URL Style' flipper
    new_url_style_cls_list = change_settings.when_flipper_switch_click('kaz')

    # THEN assert / verify if the Parent div with 'class="frm__field  fix"' has the is-checked class
    change_settings.then_assert_cls_flipper_list(new_url_style_cls_list)

    # WHEN the user clicks on the 'Site Icons' flipper
    site_icons_cls_list = change_settings.when_flipper_switch_click('kf')

    # THEN assert / verify if the Parent div with 'class="frm__field  fix"' has the is-checked class
    change_settings.then_assert_cls_flipper_list(site_icons_cls_list)

    # WHEN the user changes the Font Size
    font_size_drop = change_settings.when_dropdown_change("ks", "s")

    # THEN assert / verify that the value has actually changed
    change_settings.then_assert_dropdown_value(font_size_drop)

    # WHEN the user changes the Font Family
    font_family_drop = change_settings.when_dropdown_change("kt", "b")

    # THEN assert / verify that the value has actually changed
    change_settings.then_assert_dropdown_value(font_family_drop)
