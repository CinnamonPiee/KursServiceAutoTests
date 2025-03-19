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
    CHECK_LIST_TEXT = (By.CSS_SELECTOR, "a[href='/check-list']")
    CHECK_LIST_NUM = (By.ID, "check-list-big")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/site/login']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "a[href='/site/signup']")

    list_header_modules_visible = [HEADER, LINK_ON_MAIN_PAGE, IMG_LINK_ON_MAIN_PAGE, LINK_ON_CONTACTS_PAGE_QR,
                                   IMG_LINK_ON_CONTACTS_PAGE_QR, PHONE_NUMBER, TOWN, TOWN_ICON, TOWN_TEXT, WORKTIME,
                                   WORKTIME_ICON, WORKTIME_TEXT, CHECK_LIST_IMG, CHECK_LIST_TEXT, CHECK_LIST_NUM,
                                   LOGIN_BUTTON, SIGNUP_BUTTON]
