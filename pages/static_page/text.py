from locators.static_page_locators import StaticPageLocators
from pages.base_page import BasePage


class TextStaticPage(BasePage):
    # -----------------------------------------------
    # Проверка текста модулей на статической странице
    # -----------------------------------------------

    # Проверки текста модулей верхнего хедера
    def should_be_correct_text_header_modules_on_static_page(self) -> None:
        correct_text = ["8 (910) 448-45-06", "Москва, 1-я Мытищинская 16 с.1",
                        "Работаем: Пн-Пт с 9:00 - 20:00,\nСб с 9:00 - 17:00, Вс выходной", "ЧЕК ЛИСТ - 0", "ВХОД",
                        "РЕГИСТРАЦИЯ"]
        for text, item in zip(correct_text, StaticPageLocators.list_header_modules_text):
            assert self.text_element_is_correct(
                *item,
                text,
            ), f"Test crashed due to invalid text '{text}'"

    # Проверки текста модулей кнопок справа
    def should_be_correct_text_right_modules_on_static_page(self) -> None:
        correct_text = ["ЭВАКУАЦИЯ", "КОНТАКТЫ"]
        for text, item in zip(correct_text, StaticPageLocators.list_right_modules_text):
            assert self.text_element_is_correct(
                *item,
                text,
            ), f"Test crashed due to invalid text '{text}'"

    # Проверки текста модулей кнопок слева
    def should_be_correct_text_left_modules_on_static_page(self) -> None:
        correct_text = ["ЗАПИСЬ НА ТЕХ. ОБСЛ.", "ДИАГНОСТИКА", "ШИНСЕРВИС"]
        for text, item in zip(correct_text, StaticPageLocators.list_left_modules_text):
            assert self.text_element_is_correct(
                *item,
                text,
            ), f"Test crashed due to invalid text '{text}'"

    # Проверки текста модулей футера снизу
    def should_be_correct_text_footer_modules_on_static_page(self) -> None:
        correct_text = ["8 (910) 448-45-06", "МОСКВА, 1-Я МЫТИЩИНСКАЯ 16 С.1", "ЗАПИСЬ НА ТЕХ. ОБСЛУЖИВАНИЕ",
                        "ЗАПИСЬ НА ДИАГНОСТИКУ", "ЗАПИСЬ НА ШИНОМАНТАЖ", "ЗАПИСЬ НА СХОД-РАЗВАЛ", "ЗАПИСЬ НА ЭВАКУАЦИЮ",
                        "КОНТАКТЫ", "О СЕРВИСЕ", "СТРАХОВАНИЕ", "ОТЗЫВЫ", "ГАРАНТИЯ",
                        "© 2020г. https://kurs-service.ru - прозрачный автосервис у нас один курс. All Rights Reserved.\nСайт не является публичной офертой и носит информационный характер."]
        for text, item in zip(correct_text, StaticPageLocators.list_footer_modules_text):
            assert self.text_element_is_correct(
                *item,
                text,
            ), f"Test crashed due to invalid text '{text}'"
