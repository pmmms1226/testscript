import os
import pytest
from selenium import webdriver

def pytest_addoption(parser):
   parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
   parser.addoption("--url", action="store", default="https://www.google.com/", help="url")
   

@pytest.fixture(scope="module", autouse=True)
def driver(request):
   browser = request.config.getoption("--driver")
   if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        myos = "mac"
        #browser = webdriver.Chrome(os.getcwd()+'/driver/chromedriver_'+myos, chrome_options=options)
        browser = webdriver.Chrome(os.getcwd()+'/driver/chromedriver_'+myos)
        browser.implicitly_wait(3)
        return browser
   else:
       print ('only chrome is supported at the moment')

# @pytest.fixture(scope="module")
# def username(request):
#    return request.config.getoption("--username")


# @pytest.fixture(scope="module")
# def password(request):
#    return request.config.getoption("--password")


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")



   