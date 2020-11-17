import pytest
from selenium import webdriver
from Git.Config.config import TestData


@pytest.fixture(params=["chrome, firefox"], scope='class')
def init_driver(request):
    if request.params == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.Ch_exe_path)
    if request.params == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.Fi_exe_path)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(50)
    yield
    web_driver.close()
