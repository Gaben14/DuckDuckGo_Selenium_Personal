"""
This module contains the DuckDuckGoSearch (https://duckduckgo.com) settings page.
"""

import pytest
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains


class DuckDuckGoSettings:
    # Locators:
    SETTINGS = (By.CSS_SELECTOR, 'div.dropdown > a.zcm__link')
    DARK_MODE = (By.CSS_SELECTOR, 'div[data-theme-id="d"] > label.set-theme')

    FONT_SIZE_SEL = 'setting_ks'
    FONT_FAMILY_SEL = 'setting_kt'

    is_checked = 'is-checked'
    """
    The problem here is that we need to close the autocomplete result modal
    so that we can click on settings
    """

    # Initialize:
    def __init__(self, browser: WebDriver):
        self.browser = browser

        # Move all the method calls inside duck_settings to the constructor __init__

    # Interaction Methods:
    def duck_settings(self, font_size_val, font_fam_val, lang_val, country_val):
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
        #self.flipper_switch('kav')
        # Turn on "Open Links in a New Tab" - setting_kn
        #self.flipper_switch('kn')
        # Click on Reset buttons.
        self.click_on_reset_btn()
        # Change region
        self.change_region(country_val)

    def dark_mode(self):
        # Change to Dark Mode
        dark_mode = self.browser.find_element(*self.DARK_MODE)
        dark_mode.click()

        # Assert / Verify if the Dark Mode has the is-checked class
        dark_mode_cls_list = dark_mode.get_attribute('class')
        assert self.is_checked in dark_mode_cls_list

    def flipper_switch(self, flipper_val):

        flipper = self.browser.find_element(By.CSS_SELECTOR, f'label[for="setting_{flipper_val}"]')
        flipper.click()

        # Create a local variable in which you contain the parent's CSS selector 'class="frm__field  fix"'
        container_div = flipper.find_element(By.XPATH, '../..')
        # TODO - Assert / Verify if the Parent div with 'class="frm__field  fix"' has the is-checked class
        container_div_cls_list = container_div.get_attribute('class')

        if self.is_checked in container_div_cls_list:
            assert self.is_checked in container_div_cls_list
        else:
            assert self.is_checked not in container_div_cls_list

    def dropdown_change(self, select_container, select_val):
        # Change the Font Size or Font-Family depending on the parameter
        sel_container = self.browser.find_element(By.ID, select_container)
        sel_container.click()

        sel_option = self.browser.find_element(By.CSS_SELECTOR, f'#{select_container} > option[value="{select_val}"]')
        sel_option_value = sel_option.get_attribute('value')
        sel_option.click()

        # TODO -  Assert that value has actually changed
        assert sel_option_value == select_val


    def click_on_reset_btn(self):
        # Click on Reset inside the class: .settings-dropdown--header
        reset_btn = self.browser.find_elements(By.CSS_SELECTOR, '.settings-dropdown--header > a')

        for btn in reset_btn:
            btn.click()

        # TODO - Assert if values are back to normal

    # Assert For later: Save the values of these settings change, refresh the page.
    # Check if the values are the same ?
    def change_region(self, country):
        region_btn = self.browser.find_element(By.CSS_SELECTOR, '.dropdown--region > a')
        region_btn.click()

        # Select one of the Countries inside the region
        country = self.browser.find_element(By.XPATH, f'//a[text()="{country}"]')
        country.click()

        # TODO - Assert if the country has really changed.

        # Reset all settings
        reset_flip = self.browser.find_element(By.CLASS_NAME, 'switch__knob')
        reset_flip.click()
