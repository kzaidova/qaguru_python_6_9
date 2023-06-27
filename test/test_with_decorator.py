from allure_commons.types import Severity
from selene import browser, by, be
import pytest
import allure

@allure.label("owner", "k_zaidova")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('With decorators')

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_height = '1440'
    browser.config.window_width = '1080'


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number('#65')
    closing_browser()

@allure.step("Открываем главую страницу GitHub")
def open_main_page():
    browser.open("https://github.com/")

@allure.step("Открываем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()

@allure.step("Кликаем по ссылке репозиторий")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step("Открываем Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()

@allure.step("Закрываем браузер")
def closing_browser():
    browser.quit()
