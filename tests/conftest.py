import os

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
        help="Choose language to open the site",
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
    # options_chrome.add_argument(
        # "--window-size=1920,1080") # Устанавливает разрешение окна для отображения всех элементов
    options_chrome.add_argument("--headless")  # Делает браузер невидимым
    options_chrome.add_argument("--no-sandbox")  # Для работы в контейнере
    options_chrome.add_argument("--disable-dev-shm-usage")  # Для работы в контейнере
    options_chrome.add_argument(f"--user-data-dir=/tmp/chrome-user-{os.getpid()}")  # Уникальный профиль

    if browser_name == "chrome":
        print("\nStart Chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)

    elif browser_name == "yandex":
        print("\nStart Yandex browser for test..")
        browser = webdriver.Chrome(options=options_chrome)

    elif browser_name == "safari":
        print("\nStart Safari browser for test..")
        browser = webdriver.Safari()

    else:
        raise pytest.UsageError("--browser should be chrome, yandex, or safari")

    yield browser
    print("\nQuit browser..")
    browser.quit()
