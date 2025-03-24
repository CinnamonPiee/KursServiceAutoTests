import re
from typing import Any

from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementNotInteractableException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.csv_config import log_csv_error
from utils.logger_config import get_logger


class BasePage:
    def __init__(self, browser, page_name=None, url=None, timeout=0) -> None:
        self.browser: Any = browser
        self.browser.implicitly_wait(timeout)  # Стоит 0, так как в каждой функции за ожидание отвечает WebDriverWait
        self.url: Any = url
        self.page_name = page_name
        self.logger = get_logger(self.page_name)

    def log_info(self, message):
        """Логирует информационное сообщение"""
        self.logger.info(f"{message}")

    def log_warning(self, message):
        """Логирует сообщение об предупреждении"""
        self.logger.warning(f"{message}")
        log_csv_error(self.page_name, message, self.url)

    def log_error(self, message):
        """Логирует сообщение об ошибке"""
        self.logger.error(f"{message}")
        log_csv_error(self.page_name, message, self.url)

    def open(self) -> None:
        """Открывает страницу по указанному URL и логирует событие"""
        if self.url:
            self.logger.info(f"✅✅✅ Открываю страницу: {self.url} для тестов ✅✅✅")
            self.browser.get(self.url)
        else:
            self.logger.error("Не указан URL для открытия страницы.")
            log_csv_error(self.page_name, "Не указан URL для открытия страницы.", self.url)

    # ----------------
    # Функции проверок
    # ----------------

    # Проверка на наличие элемента на странице
    def is_element_present(self, how, what, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((how, what))
            )
            self.logger.info(f"✅ Элемент найден: {what}")
            return True
        except TimeoutException:
            self.logger.warning(f"⚠️ Элемент НЕ найден: {what}")
            log_csv_error(self.page_name, f"⚠️ Элемент НЕ найден: {what}", self.url)
            return False

    # Проверка, что элемент не появиться через определенное время
    def is_not_element_present(self, how, what, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((how, what))
            )
            self.logger.info(f"⚠️ Элемент появился (как и ожидалось): {what}")
            return False
        except TimeoutException:
            self.logger.warning(f"✅ Элемент НЕ появился: {what}")
            return True

    # Проверка, что какой-то элемент исчезнет через определенное время
    def is_disappeared(self, how, what, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 0.5, [TimeoutException]).until_not(
                ec.presence_of_element_located((how, what))
            )
            self.logger.info(f"✅ Элемент исчез (как ожидалось): {what}")
            return True
        except TimeoutException:
            self.logger.warning(f"⚠️ Элемент НЕ исчез за {timeout} сек.: {what}")
            return False

    # Проверка, что элемент отображается
    def is_element_displayed(self, how, what, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located((how, what))
            )
            self.logger.info(f"✅ Элемент отображается: {what}")
            return True
        except TimeoutException:
            self.logger.warning(f"⚠️ Элемент НЕ отображается: {what}")
            return False

    # Проверка отображения элемента определенное время
    def is_element_displayed_per_time(self, how, what, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located((how, what))
            )
            self.logger.info(
                f"✅ Элемент отображался в течение {timeout} секунд: {what}"
            )
            return True
        except TimeoutException:
            self.logger.warning(
                f"⚠️ Элемент НЕ отображался в течение {timeout} секунд: {what}"
            )
            return False

    # Проверка доступности элемента на странице
    def element_is_enabled(self, how, what, timeout=5) -> bool:
        try:
            element = WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((how, what))
            )
            is_enabled = element.is_enabled()
            if is_enabled:
                self.logger.info(f"✅ Элемент доступен: {what}")
            else:
                self.logger.warning(f"⚠️ Элемент найден, но НЕ доступен: {what}")
            return is_enabled
        except (NoSuchElementException, TimeoutException):
            self.logger.error(f"⚠️ Элемент НЕ найден или НЕ доступен: {what}")
            return False

    # Проверка корректности текста у элемента
    def text_element_is_correct(self, how, what, text, timeout=5) -> bool:
        try:
            element = WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located((how, what))
            )
            actual_text = (element.text or "").strip()
            is_correct = actual_text == text
            if is_correct:
                self.logger.info(
                    f'✅ Текст элемента корректен: {what} ("{actual_text}")'
                )
                return True
            else:
                self.logger.warning(
                    f'⚠️ Текст элемента НЕ совпадает: {what} (Ожидалось: "{text}", Получено: "{actual_text}")'
                )
                log_csv_error(self.page_name,
                              f'⚠️ Текст элемента НЕ совпадает: {what} (Ожидалось: "{text}", Получено: "{actual_text}")',
                              self.url)
                return False
        except TimeoutException:
            self.logger.warning(f"⚠️ Элемент НЕ найден или НЕ видим: {what}")
            log_csv_error(self.page_name, f"⚠️ Элемент НЕ найден или НЕ видим: {what}", self.url)
            return False

    # Проверка атрибута элемента
    def is_element_attribute_correct(
            self, how, what, attribute, text, timeout=5
    ) -> bool | None:
        try:
            element = WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located((how, what))
            )
            actual_value = element.get_attribute(attribute) or ""
            is_correct = actual_value == text
            if is_correct:
                self.logger.info(
                    f"✅ Атрибут '{attribute}' у элемента {what} имеет правильное значение: \"{actual_value}\""
                )
                return True
            else:
                self.logger.warning(
                    f'⚠️ Атрибут \'{attribute}\' у элемента {what} НЕ совпадает. Ожидалось: "{text}", Получено: "{actual_value}"'
                )
                return False
        except TimeoutException:
            self.logger.error(f"⚠️ Элемент НЕ найден или НЕ видим: {what}")
            return False

    # Проверка редиректа статических ссылок и открытия новой вкладки.
    def is_redirect_correct(self, old_url, new_url, old_tabs, timeout=5) -> bool:
        try:
            new_tabs = self.browser.window_handles
            is_new_tab_opened = len(new_tabs) > len(old_tabs)
            if is_new_tab_opened:
                self.browser.switch_to.window(new_tabs[-1])
            WebDriverWait(self.browser, timeout).until(
                lambda driver: driver.current_url != old_url
            )
            current_url = self.browser.current_url
            if new_url == current_url:
                self.logger.info(f"✅ Успешный редирект: {old_url} → {new_url}")
                return True
            else:
                self.logger.warning(
                    f"⚠️ Неверный редирект: ожидалось {new_url}, но перешли на {current_url}"
                )
                return False
        except TimeoutException:
            self.logger.error(
                f"⚠️ Редирект НЕ произошёл. Остался URL: {self.browser.current_url}"
            )
            return False

    # Проверка редиректа с учётом динамических URL и открытия новой вкладки.
    def is_redirect_dynamic_correct(
            self, old_url, new_url, old_tabs, timeout=5
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda driver: len(driver.window_handles) > len(old_tabs)
                               or driver.current_url != old_url
            )
            new_tabs = self.browser.window_handles
            if len(new_tabs) > len(old_tabs):
                self.browser.switch_to.window(new_tabs[-1])
            WebDriverWait(self.browser, timeout).until(
                lambda driver: driver.current_url != old_url
            )
            current_url = self.browser.current_url
            if re.search(new_url, current_url):
                self.logger.info(f"✅ Успешный редирект: {old_url} → {current_url}")
                return True
            else:
                self.logger.warning(
                    f"⚠️ Неверный редирект: ожидалось {new_url}, но перешли на {current_url}"
                )
                return False
        except TimeoutException:
            self.logger.error(
                f"⚠️ Редирект НЕ произошёл. Остался URL: {self.browser.current_url}"
            )
            return False

    # Проверка кликабельности элемента
    def is_element_to_be_clickable(self, how, what, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable((how, what))
            )
            self.logger.info(
                f"✅ Элемент кликабелен: {what} (Таймаут: {timeout} секунд)"
            )
            return True
        except (TimeoutException, ElementNotInteractableException):
            self.logger.error(f"⚠️ Элемент НЕ кликабелен: {what}")
            return False

    # Проверяет, что всплывающее предупреждение появилось и содержит нужный текст.
    def should_see_popup_with_text(self, how, what, text, expected_text, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located((how, what))
            )
            text = text.strip()
            if text == expected_text:
                self.logger.info(
                    f"✅ Предупреждение '{expected_text}' в элементе {what} имеет корректный текст: \"{text}\""
                )
                return True
            else:
                self.logger.warning(
                    f'⚠️ Предупреждение в элементе {what} содержит некорректный текст. Ожидалось: "{expected_text}", Получено: "{text}"'
                )
                return False
        except TimeoutException:
            self.logger.error(
                f"⚠️ Всплывающее предупреждение не появилось в элементе {what} за {timeout} секунд. Ожидалось: '{expected_text}'"
            )
            return False
