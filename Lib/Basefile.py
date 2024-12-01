from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def __init__(self,driver):
        self.driver = driver
        self.wait_obj = WebDriverWait(driver,10)

    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def switch_window(self,window_num):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[window_num])

    def select_item(self,locator,item):
            element = self.driver.find_element(*locator)
            select = Select(element)
            select.select_by_visible_text(item)

    def wait_for_element(self,otp): # validate OTP popup is displayed or not
        try:
            self.wait_obj.until(Ec.presence_of_element_located(otp))
            print(f"Element{otp} is visible")
        except Exception as e:
            raise AttributeError(f"Element {otp} not visible")

    def click_elements(self,locator):
        self.driver.find_elements(*locator)

    # def calendar_popup(self,locator,year,month,date):
    #     calendar_field = self.wait_obj.until(Ec.element_to_be_clickable(locator))
    #     calendar_field.click()
    #
    #     year_dropdown = self.wait_obj.until(Ec.element_to_be_clickable(*locator,year)
    #     year_dropdown.click()


