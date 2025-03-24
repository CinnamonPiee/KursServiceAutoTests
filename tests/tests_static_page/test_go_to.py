import pytest

from pages.static_page.go_to import GoToStaticPage


@pytest.mark.static_page_go_to
@pytest.mark.static_page
class TestStaticPage:
    # ----------------------------------------------------------
    # Тесты редиректа на другие страницы со статической страницы
    # ----------------------------------------------------------

    # ----------------------------------------------------
    # Тесты редиректа на другие страницы с верхнего хедера
    # ----------------------------------------------------

    link: str = "https://kurs-service.ru/"
    page_name: str = "go_to_static_page"

    # Тест редиректа на главную страницу со статической страницы
    @pytest.mark.xfail(
        strict=False,
        reason="If the test failed, then it worked as it should, because the page changed to the same page.",
    )
    def test_redirect_must_be_made_on_main_page_from_static_page(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_main_page_from_static_page()

    # Тест редиректа на страницу контактов со статической страницы
    def test_redirect_must_be_made_on_contacts_page_from_static_page(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_contacts_page_from_static_page()

    # Тест редиректа на страницу чек листа со статической страницы
    def test_redirect_must_be_made_on_check_list_page_from_static_page(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_check_list_page_from_static_page()

    # Тест редиректа на страницу авторизации со статической страницы
    def test_redirect_must_be_made_on_login_page_from_static_page(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_login_page_from_static_page()

    # Тест редиректа на страницу регистрации со статической страницы
    def test_redirect_must_be_made_on_signup_page_from_static_page(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_signup_page_from_static_page()

    # --------------------------------------------------
    # Тесты редиректа на другие страницы с кнопок справа
    # --------------------------------------------------

    # Тест редиректа на страницу контактов со статической страницы кнопок справа
    def test_redirect_must_be_made_on_contacts_page_from_static_page_right_button(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_contacts_page_from_static_page_right_button()

    # ---------------------------------------------------
    # Тесты редиректа на другие страницы с нижнего футера
    # ---------------------------------------------------

    # Тест редиректа на страницу карты со статической страницы кнопок справа
    def test_redirect_must_be_made_on_yandex_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_yandex_page_from_static_page_footer()

    # Тест редиректа на страницу контакты (индекс) со статической страницы кнопок справа
    def test_redirect_must_be_made_on_contacts_index_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_contacts_index_page_from_static_page_footer()

    # Тест редиректа на страницу нас (индекс) со статической страницы кнопок справа
    def test_redirect_must_be_made_on_about_index_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_on_about_index_page_from_static_page_footer()

    # Тест редиректа на страницу страхование (индекс) со статической страницы кнопок справа
    def test_redirect_must_be_made_insurance_index_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_insurance_index_page_from_static_page_footer()

    # Тест редиректа на страницу отзывы (индекс) со статической страницы кнопок справа
    def test_redirect_must_be_made_reviews_index_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_reviews_index_page_from_static_page_footer()

    # Тест редиректа на страницу гарантии (индекс) со статической страницы кнопок справа
    def test_redirect_must_be_made_warranty_index_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_warranty_index_page_from_static_page_footer()

    # Тест редиректа на страницу инстаграм со статической страницы кнопок справа
    def test_redirect_must_be_made_instagram_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_instagram_page_from_static_page_footer()

    # Тест редиректа на страницу фейсбука со статической страницы кнопок справа
    def test_redirect_must_be_made_facebook_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_facebook_page_from_static_page_footer()

    # Тест редиректа на страницу вконтакте со статической страницы кнопок справа
    def test_redirect_must_be_made_vk_page_from_static_page_footer(self, browser) -> None:
        page = GoToStaticPage(browser, page_name=self.page_name, url=self.link)
        page.open()
        page.a_redirect_must_be_made_vk_page_from_static_page_footer()
