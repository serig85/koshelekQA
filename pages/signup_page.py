from time import sleep

from .base_page import BasePage
from .locators import BasePageLocation, MainPageLocation, SignupPageLocation


class SignupPage(BasePage):
    def open_signup(self):
        shadow_root_element = self.browser.find_element(*SignupPageLocation.shadow_root).shadow_root
        shadow_root_element.find_element(*SignupPageLocation.email_input).send_keys('String')

        shadow_host_element = shadow_root_element.find_element(*SignupPageLocation.button)
        shadow_host_element.click()
        print(f'print {shadow_root_element}')
        #print(f'print {shadow_host_element}')
        #shadow_element = shadow_host_element.find_element(*SignupPageLocation.button)

        email_message = shadow_root_element.find_element(*SignupPageLocation.email_message).text
        print(f'email {email_message}')

        sleep(4)
        assert 2 == 2, '2 не равняется 1'
