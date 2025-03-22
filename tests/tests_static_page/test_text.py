import pytest

from pages.static_page.text import TextStaticPage


@pytest.mark.static_page_text
@pytest.mark.static_page
class TestStaticPage:
    # --------------------------------------------
    # Тесты текста модулей на статической странице
    # --------------------------------------------

    link: str = "https://kurs-service.ru/"
    page_name: str = "text_static_page"

    # Тест текста модулей верхнего хедера
    def test_check_correct_text_header_modules_on_static_page(self, browser) -> None:
        page = TextStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_correct_text_header_modules_on_static_page()

    # Тест текста модулей кнопок справа
    def test_check_correct_text_right_modules_on_static_page(self, browser) -> None:
        page = TextStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_correct_text_right_modules_on_static_page()

    # Тест текста модулей кнопок слева
    def test_check_correct_text_left_modules_on_static_page(self, browser) -> None:
        page = TextStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_correct_text_left_modules_on_static_page()

    # Тест текста модулей футера снизу
    def test_check_correct_text_footer_modules_on_static_page(self, browser) -> None:
        page = TextStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_correct_text_footer_modules_on_static_page()