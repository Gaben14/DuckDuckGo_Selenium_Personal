"""
This module contains the shared fixtures,
which can be used by every file in the project.
"""
import json
import pytest
import selenium.webdriver
from selenium.webdriver.firefox.options import Options
# For custom firefox configuration.
from pages.search_page import DuckDuckGoSearchPage


@pytest.fixture
def config(scope="session"):
    # Read the configs from the config.json file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert which browser values are acceptable coming from the config.json file
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    # Checking if the value is int
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return value
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        opts = Options()
        opts.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = selenium.webdriver.Firefox(executable_path=r'C:\Selenium\geckodriver.exe', options=opts)
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Configure the implicit wait between test method calls:
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup:
    driver.quit()


@pytest.fixture()
def open_page(browser):
    search_page = DuckDuckGoSearchPage(browser)

    # PHRASES to search for - Update to parametrize later!
    PHRASE = 'panda'

    # GIVEN The DuckDuckGo page is displayed
    search_page.load()

    # WHEN the user searches for a single "phrase"
    search_page.search_single_phrase(PHRASE)
