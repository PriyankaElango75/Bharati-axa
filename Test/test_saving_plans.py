# from time import sleep
#
# from TestData.Excel import read_locators,read_agent_code
# from POM.Savingplans import SavingPlans
# from Lib.Basefile import BaseClass
#
#
# def test_saving_plan(_driver):
#     base_obj = BaseClass(_driver)
#     sav_obj = SavingPlans(_driver)
#     saving_xpath = sav_obj.saving_plan()
#     saving_plan_name = ["Elite Advantage"]
#     for plan in saving_xpath:
#         if plan in saving_plan_name:
#             plans = f"//div[@id='row-SavingsPlans']/..//div[text()='{plan}']"
#             base_obj.click_element(plans)
#             sleep(3)