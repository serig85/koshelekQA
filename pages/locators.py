from selenium.webdriver.common.by import By


class BasePageLocation:
    pass


class MainPageLocation:
    button_signup = (By.XPATH, '//div[@class="k-btn-header-signup"]')


class SignupPageLocation:
    shadow_root = (By.CSS_SELECTOR, '[class = "remoteComponent"]')
    switch_viewport = (By.XPATH, '//div[@data-wi="viewport"]')
    check_box_agree = (By.XPATH, '//div[@class="v-input--selection-controls__input"]')
    button = (By.CSS_SELECTOR, '[type="submit"]')
    email_input = (By.CSS_SELECTOR, 'div[data-wi="identificator"] input')
    email_message = (By.CSS_SELECTOR, 'div[data-wi="identificator"] div[data-wi="message"]')
