from allure_commons.types import Severity
from selene import browser, by, be
import pytest
import allure
@allure.story('just selene')
@allure.label("owner", "k_zaidova")
@allure.tag('web')
@allure.severity(Severity.NORMAL)

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_height = '1440'
    browser.config.window_width = '1080'

def test_github():
    browser.open("https://github.com/")

    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#65")).should(be.visible)

    browser.quit()


