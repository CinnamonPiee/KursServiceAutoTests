import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or yandex or safari",
    )
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Choose language what you want to open the site",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")

    options_chrome = OptionsChrome()
    options_chrome.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )
    # options_chrome.add_argument("--start-fullscreen") # Запускает тесты в полноэкранном режиме
    # если отключена настройка о невидимости браузера
    options_chrome.add_argument(
        "--window-size=1920,1080")  # Устанавливает разрешение окна для отображения всех элементов
    options_chrome.add_argument("--headless")  # Делает браузер невидимым

    if browser_name == "chrome":
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    # TODO Не работает браузер Яндекс, решить проблему
    elif browser_name == "yandex":
        print("\nstart Yandex browser for test..")
        options_chrome.binary_location = (
            "/Applications/Yandex.app/Contents/MacOS/Yandex"
        )
        browser = webdriver.Chrome(options=options_chrome)
    # TODO Создать по браузер Safari
    else:
        raise pytest.UsageError("--browser_name should be chrome or yandex or safari")

    yield browser

    print("\nquit browser..")
    browser.quit()
