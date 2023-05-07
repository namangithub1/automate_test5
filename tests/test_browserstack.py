import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


# Command to run: 
#   Test 5:
#       cd "/Users/namanchaturvedi/Documents/Product onboarding/automate/test5/"
#       paver run browserstack


# Define passwords
@pytest.fixture(params=["correct","incorrect"])
def login(request):
    login_deets = ["","",""]
    if request.param == "correct":
        login_deets = ["nc11@iitbbs.ac.in","namanbrowserstack","right"]
    elif request.param == "incorrect":
        login_deets = ["bj20150@astra.xlri.ac.in","namanbrdgffghowserstack","wrong"]
    return login_deets


def test_example(driver,login):
    with pytest.raises(TimeoutException) as couldNotLoad:
        
    # for login_i in login_list:
        browser_i = driver.name
        login_deets = login
        login_i = login[2]
        
        test_email = login_deets[0]
        test_password = login_deets[1]
        sign_in_url = 'https://www.browserstack.com/users/sign_in';
        driver.get(sign_in_url)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'user_email_login')))
        raise TimeoutException('Could not load the sign in website in ',driver.name)

    with pytest.raises(NoSuchElementException):
        # Enter your login credentials and click the login button
        driver.find_element("id", "user_email_login").send_keys(test_email)
        # find password input field and insert password as well
        driver.find_element("id", "user_password").send_keys(test_password)
        # click login button
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'commit')))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        if driver.current_url == sign_in_url: 
            element.click()
        raise NoSuchElementException('Could not load the sign in website in ',driver.name)
    


    WebDriverWait(driver, 20)

    live_dashboard_url = 'https://live.browserstack.com'
    
    if live_dashboard_url not in driver.current_url:
        driver.get(live_dashboard_url)

    WebDriverWait(driver, 10)

    with pytest.raises(AssertionError):
        live_dashboard_url in driver.current_url
        raise AssertionError(browser_i,':\n\tFail: Login for ',login_i,'\n')

    if live_dashboard_url in driver.current_url:
        print(browser_i,':\n\tPass: Login for ',login_i,'\n')

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="platform-list-react"]/div/div[1]/div/div[4]/div[1]/div')))
        element.click()

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="platform-list-react"]/div/div[2]/div/div[2]/div[4]/div[1]/div[5]/div/div')))
        element.click()

        print(browser_i,':\n\tPass: Dashboard for ',login_i,'\n')
    else:
        print(browser_i,':\n\tFail: Login for ',login_i,'\n')

    