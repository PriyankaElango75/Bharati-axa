from time import sleep
from selenium import webdriver
from Lib.Basefile import BaseClass
# from TestData.Excel import read_locators,read_agent_code,read_elite_plan


class EliteAdvantage:

    def __init__(self,driver):
        self.driver = driver
        self.base_obj = BaseClass(driver)

    def elite_plan(self,firstname,gender,ageproof):
        self.base_obj.click_element(("xpath","//div[text()='Elite Advantage']"))
        sleep(2)
        self.base_obj.enter_text(("id","txtLifeAssuredFirstName"),firstname)
        self.base_obj.select_item(("xpath","//select[@id='ddlLI_GENDER']"),gender)
        self.base_obj.select_item(("xpath","//select[@id='ddlAgeProof']"),ageproof)
        self. 



