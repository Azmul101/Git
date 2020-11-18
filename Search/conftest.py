import pytest
from selenium import webdriver
from Git.Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def driver_init(request):
    web_driver = webdriver.Chrome(executable_path=TestData.Ch_exe_path)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass


