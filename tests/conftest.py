import pytest
from selene import command
from selene.support.conditions import have
from selene.support.shared import browser

#задаем размер окна браузера. Для этого проекта размер имеет значение.
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    yield


@pytest.fixture()
def open_and_quit_browser_automation_practice_form():
    browser.open('/automation-practice-form')
    #проверяем наличие рекламных блоков
    ads = browser.all('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
    if ads.with_(timeout=2).wait.until(have.size_greater_than_or_equal(1)):
        ads.perform(command.js.remove)
    yield
    browser.quit()
