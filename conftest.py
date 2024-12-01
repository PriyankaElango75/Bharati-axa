
from selenium.webdriver.chrome.webdriver import WebDriver as chrome
from selenium.webdriver.firefox.webdriver import WebDriver as firefox
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",dest = "browser",action = "store",default = "chrome")

@pytest.fixture
def _driver(request):
    _browser = request.config.option.browser.upper()
    if _browser == "CHROME":
        driver = chrome()
    elif _browser == "FIREFOX":
        driver = firefox()
    else:
        raise Exception("Unknown Browser")

    driver.maximize_window()
    driver.get("https://msell-uat.bhartiaxa.com/MSell/Product.aspx")
    yield driver
    driver.quit()
