from locators.static_page_locators import StaticPageLocators
from pages.base_page import BasePage


class VisibleStaticPage(BasePage):
    # ----------------------------------------------------
    # Проверка отображения модулей на статической странице
    # ----------------------------------------------------

    # Проверки отображения модулей верхнего хедера
    def should_be_visible_header_modules_on_static_page(self) -> None:
        for item in StaticPageLocators.list_header_modules_visible:
            assert self.is_element_present(*item), f"{item} is not visible on page!"

    # Проверки отображения модулей кнопок справа
    def should_be_visible_right_modules_on_static_page(self) -> None:
        for item in StaticPageLocators.list_right_modules_visible:
            assert self.is_element_present(*item), f"{item} is not visible on page!"

    # Проверки отображения модулей кнопок слева
    def should_be_visible_left_modules_on_static_page(self) -> None:
        for item in StaticPageLocators.list_left_modules_visible:
            assert self.is_element_present(*item), f"{item} is not visible on page!"

    # Проверки отображения модулей нижнего футера
    def should_be_visible_footer_module_on_static_page(self) -> None:
        for item in StaticPageLocators.list_footer_modules_visible:
            assert self.is_element_present(*item), f"{item} is not visible on page!"
