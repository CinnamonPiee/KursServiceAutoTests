from locators.static_page_locators import StaticPageLocators
from pages.base_page import BasePage


class GoToStaticPage(BasePage):
    # -------------------------------------------------------------
    # Проверка редиректа на другие страницы со статической страницы
    # -------------------------------------------------------------

    # -------------------------------------------------------
    # Проверка редиректа на другие страницы с верхнего хедера
    # -------------------------------------------------------

    # Проверки редиректа на главную страницу со статической страницы
    def a_redirect_must_be_made_on_main_page_from_static_page(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.LINK_ON_MAIN_PAGE).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/ page did not occur!"

    # TODO при нажатии на номер телефона открывается приложение (в зависимости от устройства)

    # Проверка редиректа на страницу контактов со статической страницы
    def a_redirect_must_be_made_on_contacts_page_from_static_page(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.LINK_ON_CONTACTS_PAGE_QR).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/contacts",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/contacts page did not occur!"

    # Проверка редиректа на страницу чек листа со статической страницы
    def a_redirect_must_be_made_on_check_list_page_from_static_page(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.CHECK_LIST_LINK).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/check-list",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/check-list page did not occur!"

    # Проверка редиректа на страницу авторизации со статической страницы
    def a_redirect_must_be_made_on_login_page_from_static_page(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.LOGIN_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/site/login",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/site/login page did not occur!"

    # Проверка редиректа на страницу регистрации со статической страницы
    def a_redirect_must_be_made_on_signup_page_from_static_page(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.SIGNUP_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/site/signup",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/site/signup page did not occur!"

    # -----------------------------------------------------
    # Проверка редиректа на другие страницы с кнопок справа
    # -----------------------------------------------------

    # Проверка редиректа на страницу контакты со статической страницы кнопок справа
    def a_redirect_must_be_made_on_contacts_page_from_static_page_right_button(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.CONTACTS_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/contacts",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/contacts page did not occur!"

    # ------------------------------------------------------
    # Проверка редиректа на другие страницы с нижнего футера
    # ------------------------------------------------------

    # TODO при нажатии на номер телефона открывается приложение (в зависимости от устройства)

    # Проверка редиректа на страницу карты со статической страницы футера снизу
    def a_redirect_must_be_made_on_yandex_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.YANDEX_ADDRESS_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://yandex.com.ge/maps/213/moscow/?ll=37.591470%2C55.816197&mode=usermaps&source=constructorLink&um=constructor%3A4c4f581d8acc2a9cbee785bedc67ec7b71da3f375886ee79e8f95aa87f5188ab&z=10",
            old_tabs,
        ), f"Redirect https://yandex.com.ge/maps/213/moscow/?ll=37.591470%2C55.816197&mode=usermaps&source=constructorLink&um=constructor%3A4c4f581d8acc2a9cbee785bedc67ec7b71da3f375886ee79e8f95aa87f5188ab&z=10 page did not occur!"

    # Проверка редиректа на страницу контакты (индекс) со статической страницы футера снизу
    def a_redirect_must_be_made_on_contacts_index_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.CONTACTS_FOOTER_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/contacts/index",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/contacts/index page did not occur!"

    # Проверка редиректа на страницу о нас (индекс) со статической страницы футера снизу
    def a_redirect_must_be_made_on_about_index_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.ABOUT_SERVICE_FOOTER_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/about/index",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/about/index page did not occur!"

    # Проверка редиректа на страницу страхование (индекс) со статической страницы футера снизу
    def a_redirect_must_be_made_insurance_index_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.INSURANCE_FOOTER_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/insurance/index",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/insurance/index page did not occur!"

    # Проверка редиректа на страницу отзывы (индекс) со статической страницы футера снизу
    def a_redirect_must_be_made_reviews_index_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.REVIEWS_FOOTER_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/reviews/index",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/reviews/index page did not occur!"

    # Проверка редиректа на страницу гарантии (индекс) со статической страницы футера снизу
    def a_redirect_must_be_made_warranty_index_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.WARRANTY_FOOTER_BUTTON).click()
        assert self.is_redirect_correct(
            self.url,
            "https://kurs-service.ru/warranty/index",
            old_tabs,
        ), f"Redirect https://kurs-service.ru/warranty/index page did not occur!"

    # Проверка редиректа на страницу инстаграм со статической страницы футера снизу
    def a_redirect_must_be_made_instagram_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.INSTAGRAM_LINK).click()
        assert self.is_redirect_correct(
            self.url,
            "https://www.instagram.com/kursvash/",
            old_tabs,
        ), f"Redirect https://www.instagram.com/kursvash/ page did not occur!"

    # Проверка редиректа на страницу фейсбука со статической страницы футера снизу
    def a_redirect_must_be_made_facebook_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.FACEBOOK_LINK).click()
        assert self.is_redirect_correct(
            self.url,
            "https://www.facebook.com/people/%D0%92%D0%B0%D1%88-%D0%9A%D1%83%D1%80%D1%81/pfbid0j1nsJd6cz7eCgJf9eKqkL1xHhjJYP11KPzfWdCRQsE32XyH6bg1ERPcZjRwTmBAMl/",
            old_tabs,
        ), f"Redirect https://www.facebook.com/people/%D0%92%D0%B0%D1%88-%D0%9A%D1%83%D1%80%D1%81/pfbid0j1nsJd6cz7eCgJf9eKqkL1xHhjJYP11KPzfWdCRQsE32XyH6bg1ERPcZjRwTmBAMl/ page did not occur!"

    # Проверка редиректа на страницу вконтакте со статической страницы футера снизу
    def a_redirect_must_be_made_vk_page_from_static_page_footer(self) -> None:
        old_tabs = self.browser.window_handles
        self.browser.find_element(*StaticPageLocators.VK_LINK).click()
        assert self.is_redirect_correct(
            self.url,
            "https://vk.com/id629804648",
            old_tabs,
        ), f"Redirect https://vk.com/id629804648 page did not occur!"
