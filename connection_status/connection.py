# Package Imports
import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Test-case URL
translation_url = "https://context.reverso.net/translation/"

# Selenium Variables // Dynamic Connection
capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(translation_url)
time.sleep(2)

# Requests Variables // Static Connection
headers = {'User-Agent': 'Chrome/103.0.0.0'} # used to introduce request as coming from a web-browser
r = requests.get(translation_url,headers=headers)

# Test Selenium Connection
def get_dynamic_status_code(url):
    for entry in driver.get_log('performance'):
        for k, v in entry.items():
            if k == 'message' and 'status' in v:
                msg = json.loads(v)['message']['params']
                for mk, mv in msg.items():
                    if mk == 'response':
                        response_url = mv['url']
                        response_status = mv['status']
                        if response_url == url:
                            return response_status
# print(get_dynamic_status_code(translation_url)) # 200

# Test Static Connection
def get_static_status_code(url):
    status = r.status_code
    return status
# print(get_static_status_code(translation_url)) # 200


def connection_main():
    translation_url = "https://context.reverso.net/translation/"
    dynamic = get_dynamic_status_code(translation_url)
    static = get_static_status_code(translation_url)
    if dynamic == static:
        driver.quit()
        return dynamic == static
    else:
        return False


# print(connection_main()) # True