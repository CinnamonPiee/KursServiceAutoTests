from selenium.webdriver.common.by import By


class StaticPageLocators:
    # ------------------------
    # Локаторы верхнего хедера
    # ------------------------

    HEADER = (By.ID, "header")
    LINK_ON_MAIN_PAGE = (By.CSS_SELECTOR, "a[href='/']")
    IMG_LINK_ON_MAIN_PAGE = (By.CSS_SELECTOR, "a[href='/'] > img")
    LINK_ON_CONTACTS_PAGE_QR = (By.CSS_SELECTOR, "a[href='/contacts']")
    IMG_LINK_ON_CONTACTS_PAGE_QR = (By.CSS_SELECTOR, "a[href='/contacts'] > img")
    PHONE_NUMBER = (By.ID, "phone")
    TOWN = (By.CLASS_NAME, "town")
    TOWN_ICON = (By.CSS_SELECTOR, ".town > i")
    TOWN_TEXT = (By.CSS_SELECTOR, ".town > span")
    WORKTIME = (By.CLASS_NAME, "worktime")
    WORKTIME_ICON = (By.CSS_SELECTOR, ".worktime > p > i")
    WORKTIME_TEXT = (By.CSS_SELECTOR, ".worktime > p")
    CHECK_LIST_IMG = (By.CLASS_NAME, "check-list")
    CHECK_LIST_LINK = (By.CSS_SELECTOR, ".check-list > a")
    CHECK_LIST_TEXT = (By.CSS_SELECTOR, ".check-list > a > p")
    CHECK_LIST_NUM = (By.ID, "check-list-big")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/site/login']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "a[href='/site/signup']")

    list_header_modules_visible = [HEADER, LINK_ON_MAIN_PAGE, IMG_LINK_ON_MAIN_PAGE, LINK_ON_CONTACTS_PAGE_QR,
                                   IMG_LINK_ON_CONTACTS_PAGE_QR, PHONE_NUMBER, TOWN, TOWN_ICON, TOWN_TEXT, WORKTIME,
                                   WORKTIME_ICON, WORKTIME_TEXT, CHECK_LIST_IMG, CHECK_LIST_TEXT, CHECK_LIST_NUM,
                                   LOGIN_BUTTON, SIGNUP_BUTTON]
    list_header_modules_text = [PHONE_NUMBER, TOWN_TEXT, WORKTIME_TEXT, CHECK_LIST_TEXT, LOGIN_BUTTON, SIGNUP_BUTTON]

    # ----------------------
    # Локаторы кнопок справа
    # ----------------------

    RIGHT_BUTTONS = (By.CLASS_NAME, "bottom-fix")
    ADD_TO_ORDER_EVACUATION_BUTTON = (By.CSS_SELECTOR, ".bottom-fix > a:nth-child(1)")
    ADD_TO_ORDER_EVACUATION_TEXT = (By.CSS_SELECTOR, ".bottom-fix > a:nth-child(1) > p")
    CONTACTS_BUTTON = (By.CSS_SELECTOR, ".bottom-fix > a:nth-child(2)")
    CONTACTS_TEXT = (By.CSS_SELECTOR, ".bottom-fix > a:nth-child(2) > p")
    MAIL_TO_BUTTON = (By.CSS_SELECTOR, ".bottom-fix > a:nth-child(3)")
    ADD_TO_ORDER_SERVICE = (By.CSS_SELECTOR, ".bottom-fix > a:nth-child(4)")

    list_right_modules_visible = [RIGHT_BUTTONS, ADD_TO_ORDER_EVACUATION_BUTTON, CONTACTS_BUTTON, MAIL_TO_BUTTON,
                                  ADD_TO_ORDER_SERVICE]
    list_right_modules_text = [ADD_TO_ORDER_EVACUATION_TEXT, CONTACTS_TEXT]

    # ---------------------
    # Локаторы кнопок слева
    # ---------------------

    LEFT_BUTTONS = (By.CLASS_NAME, "bottom-fix2")
    REGISTRATION_FOR_MAINTENANCE = (By.CSS_SELECTOR, ".bottom-fix2 > a:nth-child(1)")
    REGISTRATION_FOR_MAINTENANCE_TEXT = (By.CSS_SELECTOR, ".bottom-fix2 > a:nth-child(1) > p")
    DIAGNOSTICS = (By.CSS_SELECTOR, ".bottom-fix2 > a:nth-child(2)")
    DIAGNOSTICS_TEXT = (By.CSS_SELECTOR, ".bottom-fix2 > a:nth-child(2) > p")
    TIRE_SERVICE = (By.CSS_SELECTOR, ".bottom-fix2 > a:nth-child(3)")
    TIRE_SERVICE_TEXT = (By.CSS_SELECTOR, ".bottom-fix2 > a:nth-child(3) > p")

    list_left_modules_visible = [LEFT_BUTTONS, REGISTRATION_FOR_MAINTENANCE, DIAGNOSTICS, TIRE_SERVICE]
    list_left_modules_text = [REGISTRATION_FOR_MAINTENANCE_TEXT, DIAGNOSTICS_TEXT, TIRE_SERVICE_TEXT]

    # -----------------------
    # Локаторы нижнего футера
    # -----------------------

    FOOTER = (By.ID, "footer")
    FOOTER_NAV_INFO_ROW = (By.CSS_SELECTOR, "#footer > .container > .row")
    CALL_NUMBER_BUTTON = (By.CSS_SELECTOR, ".footer-nav > div:nth-child(1) > a")
    YANDEX_ADDRESS_BUTTON = (By.CSS_SELECTOR, ".footer-nav > div:nth-child(2) > a")
    FOOTER_MAP = (By.CLASS_NAME, "map")
    FOOTER_IMG = (By.CLASS_NAME, "footer-img")
    LEFT_BUTTONS_IN_FOOTER = (By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(1)")
    REGISTRATION_FOR_MAINTENANCE_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(1) > li:nth-child(1) > a")
    REGISTRATION_FOR_DIAGNOSTICS_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(1) > li:nth-child(2) > a")
    REGISTRATION_FOR_TIRE_SERVICE_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(1) > li:nth-child(3) > a")
    REGISTRATION_FOR_WHEEL_ALIGNMENT_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(1) > li:nth-child(4) > a")
    REGISTRATION_FOR_EVACUATION_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(1) > li:nth-child(5) > a")
    SITE_LOGO_IMG = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div.col-lg-4.hidden-xs > img")
    RIGHT_BUTTONS_IN_FOOTER = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(3)")
    CONTACTS_FOOTER_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(3) > li:nth-child(1) > a")
    ABOUT_SERVICE_FOOTER_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(3) > li:nth-child(2) > a")
    INSURANCE_FOOTER_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(3) > li:nth-child(3) > a")
    REVIEWS_FOOTER_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(3) > li:nth-child(4) > a")
    WARRANTY_FOOTER_BUTTON = (
        By.CSS_SELECTOR, "#footer > div > div.footer-nav > div:nth-child(3) > li:nth-child(5) > a")
    SOCIAL_NETWORK_IN_FOOTER = (By.CLASS_NAME, "social-network")
    INSTAGRAM_LINK = (By.CSS_SELECTOR, ".social-network > div.row.centered > a:nth-child(1)")
    FACEBOOK_LINK = (By.CSS_SELECTOR, ".social-network > div.row.centered > a:nth-child(2)")
    VK_LINK = (By.CSS_SELECTOR, ".social-network > div.row.centered > a:nth-child(3)")
    WHATSAPP_LINK = (By.CSS_SELECTOR, ".social-network > div.row.centered > a:nth-child(4)")
    BOTTOM_IN_FOOTER = (By.ID, "bottom-text")
    BOTTOM_IMG_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(1) > img")
    BOTTOM_TEXT_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(2) > p")
    BOTTOM_CASH_IMG_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(3) > img:nth-child(1)")
    BOTTOM_MASTER_CARD_IMG_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(3) > img:nth-child(2)")
    BOTTOM_VISA_IMG_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(3) > img:nth-child(3)")
    BOTTOM_SBERBANK_IMG_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(3) > img:nth-child(4)")
    BOTTOM_HALVA_IMG_IN_FOOTER = (By.CSS_SELECTOR, "#bottom-text > div > div:nth-child(3) > img:nth-child(5)")

    list_footer_modules_visible = [FOOTER, FOOTER_NAV_INFO_ROW, CALL_NUMBER_BUTTON, YANDEX_ADDRESS_BUTTON, FOOTER_MAP,
                                   FOOTER_IMG, LEFT_BUTTONS_IN_FOOTER, REGISTRATION_FOR_MAINTENANCE_BUTTON,
                                   REGISTRATION_FOR_DIAGNOSTICS_BUTTON, REGISTRATION_FOR_TIRE_SERVICE_BUTTON,
                                   REGISTRATION_FOR_WHEEL_ALIGNMENT_BUTTON, REGISTRATION_FOR_EVACUATION_BUTTON,
                                   SITE_LOGO_IMG, RIGHT_BUTTONS_IN_FOOTER, CONTACTS_FOOTER_BUTTON,
                                   ABOUT_SERVICE_FOOTER_BUTTON, INSURANCE_FOOTER_BUTTON, REVIEWS_FOOTER_BUTTON,
                                   WARRANTY_FOOTER_BUTTON, SOCIAL_NETWORK_IN_FOOTER, INSTAGRAM_LINK, FACEBOOK_LINK,
                                   VK_LINK, WHATSAPP_LINK, BOTTOM_IN_FOOTER, BOTTOM_IMG_IN_FOOTER,
                                   BOTTOM_TEXT_IN_FOOTER, BOTTOM_CASH_IMG_IN_FOOTER, BOTTOM_MASTER_CARD_IMG_IN_FOOTER,
                                   BOTTOM_VISA_IMG_IN_FOOTER, BOTTOM_SBERBANK_IMG_IN_FOOTER, BOTTOM_HALVA_IMG_IN_FOOTER]
    list_footer_modules_text = [CALL_NUMBER_BUTTON, YANDEX_ADDRESS_BUTTON, REGISTRATION_FOR_MAINTENANCE_BUTTON,
                                REGISTRATION_FOR_DIAGNOSTICS_BUTTON, REGISTRATION_FOR_TIRE_SERVICE_BUTTON,
                                REGISTRATION_FOR_WHEEL_ALIGNMENT_BUTTON, REGISTRATION_FOR_EVACUATION_BUTTON,
                                CONTACTS_FOOTER_BUTTON, ABOUT_SERVICE_FOOTER_BUTTON, INSURANCE_FOOTER_BUTTON,
                                REVIEWS_FOOTER_BUTTON, WARRANTY_FOOTER_BUTTON, BOTTOM_TEXT_IN_FOOTER]
