from Lib.Basefile import BaseClass
from TestData.Excel import read_data,read_headers
from POM.Loginpage import LoginPage
import pytest

headers = read_headers("test_loginpage","agentcode")
data =read_data("test_loginpage","agentcode")

@pytest.mark.parametrize(headers,data)
def test_login(_driver,agentcode,otp):
    base_obj = BaseClass(_driver)
    log_obj = LoginPage(_driver)
    log_obj.login_page(agentcode)
    log_obj.otp_displayed()
    log_obj.enter_otp(otp)
    log_obj.click_validate_otp()
    log_obj.validate_homepage()



    # log_obj.login_page(int(agent_code[0]))
    # assert log_obj.otp_displayed()
    # log_obj.enter_otp(agent_code[1])
    # log_obj.click_validate_otp()
    # assert log_obj.validate_homepage()

