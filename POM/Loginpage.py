from time import sleep
from selenium import webdriver
from Lib.Basefile import BaseClass


class LoginPage:


    def __init__(self,driver):
        self.driver = driver
        self.base_obj = BaseClass(driver)

    def login_page(self,agentcode):
        self.base_obj.click_element(("xpath","//input[@id='Mobile']"))
        self.base_obj.enter_text(("xpath","//input[@id='AGENT_CODE_OR_MOBILE']"),agentcode)
        self.base_obj.click_element(("xpath","//input[@class='sbmtbtn valchnge']"))
        sleep(3)

    def otp_displayed(self):
        try:
            self.base_obj.wait_for_element(("xpath","//h2[text()='OTP Authentication']"))
            return True
        except AttributeError:
            return False

    def enter_otp(self,otp):
        self.base_obj.enter_text(("xpath","//input[@id='OTPcode']"),otp)

    def click_validate_otp(self):
        self.base_obj.click_element(("xpath","//input[@id='authenticate']"))

    def validate_homepage(self):
        try:
            self.base_obj.wait_for_element(("xpath","//b[text()='Premium Calculators']"))
            return True
        except AttributeError:
            return False




