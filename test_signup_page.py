from .pages.signup_page import SignupPage


def test_scenario_one(browser):
    url = 'https://koshelek.ru/authorization/signup'
    page = SignupPage(browser, url)
    page.open()
    browser.maximize_window()
    page.open_signup()
