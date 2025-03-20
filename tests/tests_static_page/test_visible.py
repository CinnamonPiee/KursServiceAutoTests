import pytest

from pages.static_page.visible import VisibleStaticPage


@pytest.mark.static_page_visible
@pytest.mark.static_page
class TestStaticPage:
    # -----------------------------------------
    # Тесты отображения модулей верхнего хедера
    # -----------------------------------------

    link: str = "https://kurs-service.ru/"
    page_name: str = "visible_static_page"

    # Тест отображения модулей верхнего хедера
    def test_check_visible_header_modules_on_static_page(self, browser) -> None:
        page = VisibleStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_visible_header_modules_on_static_page()

    # Тест отображения модулей кнопок справа
    def test_check_visible_right_modules_on_static_page(self, browser) -> None:
        page = VisibleStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_visible_right_modules_on_static_page()

    # Тест отображения модулей кнопок слева
    def test_check_visible_left_modules_on_static_page(self, browser) -> None:
        page = VisibleStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_visible_left_modules_on_static_page()

    # Тест отображения модулей футера снизу
    def test_check_visible_footer_modules_on_static_page(self, browser) -> None:
        page = VisibleStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.should_be_visible_footer_module_on_static_page()
