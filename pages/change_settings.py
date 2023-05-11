"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) settings page.
"""

import pytest
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains


class DuckDuckGoSettings:
    # Locators:
    SETTINGS = (By.CSS_SELECTOR, '.dropdown > .zcm__link')
    DARK_MODE = (By.CSS_SELECTOR, 'div[data-theme-id="d"]')

    FONT_SIZE_SEL = 'setting_ks'
    FONT_FAMILY_SEL = 'setting_kt'
    """
    The problem here is that we need to close the autocomplete result modal
    so that we can click on settings
    """

    # Initialize:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods:
    def duck_settings(self, font_size_val, font_fam_val, lang_val):
        # Click / Open on the Settings <a>

        settings_a = WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(self.SETTINGS)
        )

        settings_a.click()
        # Change to Dark Mode
        dark_mode = self.browser.find_element(*self.DARK_MODE)
        dark_mode.click()

        # Trigger the "Site Icons" on and off - kf is for Site Icons
        self.flipper_switch('kf')
        # Font changes function call
        self.dropdown_change(self.FONT_SIZE_SEL, font_size_val)
        self.dropdown_change(self.FONT_FAMILY_SEL, font_fam_val)

        # Language change
        self.dropdown_change("setting_kad", lang_val)
        # Turn on "Infinite Scroll" - setting_kav
        self.flipper_switch('kav')
        # Turn on "Open Links in a New Tab" - setting_kn
        self.flipper_switch('kn')
        # Click on Reset buttons.
        self.click_on_reset_btn()

    def flipper_switch(self, flipper_val):
        flipper = self.browser.find_element(By.CSS_SELECTOR, f'label[for="setting_{flipper_val}"]')

        """
        action_icons = ActionChains(self.browser)
        action_icons.double_click(site_icons)
        action_icons.perform()
        """
        flipper.click()

    def dropdown_change(self, select_container, select_val):
        # Change the Font Size or Font-Family depending on the parameter
        font_sel = self.browser.find_element(By.ID, select_container)
        font_sel.click()

        font_item = self.browser.find_element(By.CSS_SELECTOR, f'#{select_container} > option[value="{select_val}"]')
        font_item.click()

        # TODO Assert that value has actually changed

    def click_on_reset_btn(self):
        # Click on Reset inside the class: .settings-dropdown--header
        reset_btn = self.browser.find_elements(By.CSS_SELECTOR, '.settings-dropdown--header > a')

        for btn in reset_btn:
            btn.click()

    # For later: Save the values of these settings change, refresh the page.
    # Check if the values are the same
