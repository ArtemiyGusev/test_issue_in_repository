import allure
from allure_commons.types import Severity
from selene.support.conditions import have
from selene.support.shared import browser


def test_1_issue_in_repository():
    browser.open('/SeleniumHQ/selenium').config.driver.set_window_size(1920, 1080)

    browser.s('#issues-tab').click()

    browser.s("[class*='flex-auto d-none'] [data-ga-click^='Issues, Table state, Closed']").click()

    browser.s('#issue_10885_link').should(have.text(' Feature]: do we have any plan to support Safari on grid 4'))


def test_2_issue_in_repository():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.feature("Тесты GitHub")
    allure.dynamic.story("Проверка Issue")
    allure.dynamic.link('https://github.com/SeleniumHQ/selenium', name='Testing "/SeleniumHQ/selenium"')
    with allure.step('Открываем браузер'):
        browser.open('/SeleniumHQ/selenium').config.driver.set_window_size(1920, 1080)

    with allure.step('Открываем список Issue'):
        browser.s('#issues-tab').click()

    with allure.step('Открываем список с закрытыми Issue'):
        browser.s("[class*='flex-auto d-none'] [data-ga-click^='Issues, Table state, Closed']").click()

    with allure.step('Проверяем корректность название в Issue 10885'):
        browser.s('#issue_10885_link').should(have.text(' Feature]: do we have any plan to support Safari on grid 4'))


@allure.step('Открываем браузер')
def browser_open():
    browser.open('/SeleniumHQ/selenium').config.driver.set_window_size(1920, 1080)


@allure.step('Открываем список Issue')
def click_issue_tab():
    browser.s('#issues-tab').click()


@allure.step('Открываем список с закрытыми Issue')
def click_closed_issue_tab():
    browser.s("[class*='flex-auto d-none'] [data-ga-click^='Issues, Table state, Closed']").click()


@allure.step('Проверяем корректность название в Issue 10885')
def click_closed_issue_tab():
    browser.s('#issue_10885_link').should(have.text(' Feature]: do we have any plan to support Safari on grid 4'))


@allure.tag('Web application')
@allure.severity(Severity.MINOR)
@allure.feature('Тесты GitHub')
@allure.story('Проверка Issue')
@allure.link('https://github.com/SeleniumHQ/selenium', name='Testing "/SeleniumHQ/selenium"')
def test_3_issue_in_repository():
    browser.open('/SeleniumHQ/selenium').config.driver.set_window_size(1920, 1080)

    browser.s('#issues-tab').click()

    browser.s("[class*='flex-auto d-none'] [data-ga-click^='Issues, Table state, Closed']").click()

    browser.s('#issue_10885_link').should(have.text(' Feature]: do we have any plan to support Safari on grid 4'))
