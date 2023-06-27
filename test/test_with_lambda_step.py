from allure_commons.types import Severity
from selene import browser, by, be
import pytest
import allure


@allure.label("owner", "k_zaidova")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('with selene steps')


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_height = '1440'
    browser.config.window_width = '1080'


def test_github():

    with allure.step("Открываем главую страницу GitHub"):
        browser.open("https://github.com/")

    with allure.step("Открываем репозиторий eroshenkoam/allure-example"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()

    with allure.step("Кликаем по ссылке репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Находим Issue  с номером #65"):
        browser.element(by.partial_text("#65")).should(be.visible)

    with allure.step("Закрываем браузер"):
        browser.quit()
