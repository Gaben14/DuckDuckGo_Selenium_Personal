"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) settings page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGoSettings:
    # Locators:
    SETTINGS = (By.CSS_SELECTOR, 'div.dropdown > a.zcm__link')
    DARK_MODE = (By.CSS_SELECTOR, 'div[data-theme-id="d"] > label.set-theme')

    FONT_SIZE_SEL = 'setting_ks'
    FONT_FAMILY_SEL = 'setting_kt'

    is_checked = 'is-checked'

    # Initialize:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods:
    def dark_mode(self):
        # WHEN the user click on the Dark Mode button (Change to Dark Mode)
        dark_mode = self.browser.find_element(*self.DARK_MODE)
        dark_mode.click()

        # THEN assert / verify if the page has changed to Dark Mode (has the is-checked class)
        dark_mode_cls_list = dark_mode.get_attribute('class')
        assert self.is_checked in dark_mode_cls_list

    def flipper_switch(self, flipper_val):
        # WHEN the user clicks on the flipper
        flipper = self.browser.find_element(By.CSS_SELECTOR, f'label[for="setting_{flipper_val}"]')
        flipper.click()

        # Create a local variable in which you contain the parent's CSS selector 'class="frm__field  fix"'
        # and it's class list
        container_div = flipper.find_element(By.XPATH, '../..')
        container_div_cls_list = container_div.get_attribute('class')

        # THEN assert / verify if the Parent div with 'class="frm__field  fix"' has the is-checked class
        if self.is_checked in container_div_cls_list:
            assert self.is_checked in container_div_cls_list
        else:
            assert self.is_checked not in container_div_cls_list

    def dropdown_change(self, select_container, select_val):
        # GIVEN the user changes the Font Size or Font-Family depending on the parameter
        sel_container = self.browser.find_element(By.ID, select_container)
        sel_container.click()

        sel_option = self.browser.find_element(By.CSS_SELECTOR, f'#{select_container} > option[value="{select_val}"]')
        sel_option_value = sel_option.get_attribute('value')
        sel_option.click()

        # THEN assert / verify that the value has actually changed
        assert sel_option_value == select_val

    def click_on_reset_btn(self):
        # WHEN the user clicks on the Reset inside the class: .settings-dropdown--header
        reset_btn = self.browser.find_elements(By.CSS_SELECTOR, '.settings-dropdown--header > a')

        for btn in reset_btn:
            btn.click()

        # THEN assert / verify if values are back to normal
        # Create the values - Open the menu for the second check
        settings_a = self.browser.find_element(*self.SETTINGS)
        settings_a.click()

        light_theme_cls_list = self.browser.find_element(By.CSS_SELECTOR,
                                                         'div[data-theme-id="-1"] > label.set-theme').get_attribute(
            'class')
        # THEN assert / verify is every value is set back to default.
        assert self.is_checked in light_theme_cls_list

        site_icons = self.browser.find_element(By.CSS_SELECTOR, 'label[for="setting_kf"')
        site_icons_cont_div_cls = site_icons.find_element(By.XPATH, "../..").get_attribute('class')
        assert self.is_checked in site_icons_cont_div_cls

        font_size = self.browser.find_element(By.CSS_SELECTOR, f'#setting_ks > option[value="n"]')
        assert font_size.get_attribute('value') == 'n'

        font_fam = self.browser.find_element(By.CSS_SELECTOR, f'#setting_kt > option[value="p"]')
        assert font_fam.get_attribute('value') == 'p'

        language = self.browser.find_element(By.CSS_SELECTOR, f'#setting_kad > option[value="wt_WT"]')
        assert language.get_attribute('value') == 'wt_WT'

        inf_scroll = self.browser.find_element(By.CSS_SELECTOR, 'label[for="setting_kav"')
        inf_scroll_cont_div_cls = inf_scroll.find_element(By.XPATH, '../..').get_attribute('class')
        assert self.is_checked not in inf_scroll_cont_div_cls

        open_new_links = self.browser.find_element(By.CSS_SELECTOR, 'label[for="setting_kn"')
        open_new_links_cont_div_cls = open_new_links.find_element(By.XPATH, '../..').get_attribute('class')
        assert self.is_checked not in open_new_links_cont_div_cls

    # Assert For later: Save the values of these settings change, refresh the page.
    def change_region(self, country):
        # WHEN the user clicks on the region button
        region_btn = self.browser.find_element(By.CSS_SELECTOR, '.dropdown--region > a')
        region_btn.click()

        # AND select one of the Countries inside the region
        country_dropdown_select = self.browser.find_element(By.XPATH, f'//a[text()="{country}"]')
        country_dropdown_select.click()

        # THEN assert / verify if the country has really changed.
        selected_country = self.browser.find_element(By.CSS_SELECTOR, 'div.dropdown--region > a').get_attribute(
            'innerHTML')
        assert selected_country == country

        # AND reset Region Settings
        reset_flip = self.browser.find_element(By.CLASS_NAME, 'switch__knob')
        reset_flip.click()

    # Handler function
    def change_duck_settings(self, font_size_val, font_fam_val, lang_val, country_val):
        # Click / Open on the Settings <a>
        settings_a = self.browser.find_element(*self.SETTINGS)
        settings_a.click()

        self.dark_mode()

        self.flipper_switch('kaz')
        # Trigger the "Site Icons" on and off - kf is for Site Icons
        self.flipper_switch('kf')
        # Font changes function call
        self.dropdown_change(self.FONT_SIZE_SEL, font_size_val)
        self.dropdown_change(self.FONT_FAMILY_SEL, font_fam_val)

        # Language change
        self.dropdown_change("setting_kad", lang_val)
        # Need to reopen the settings one more time
        settings_a = WebDriverWait(self.browser, 15).until(

            EC.element_to_be_clickable(self.SETTINGS)
        )
        settings_a.click()
        # Turn on "Infinite Scroll" - setting_kav
        self.flipper_switch('kav')
        # Turn on "Open Links in a New Tab" - setting_kn
        self.flipper_switch('kn')
        # Click on Reset buttons.
        self.click_on_reset_btn()
        # Change region
        self.change_region(country_val)
