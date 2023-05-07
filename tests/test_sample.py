import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Command to run: cd /Users/namanchaturvedi/Documents/Product onboarding/pytest-browserstack
# paver run sample


@pytest.fixture(params=["correct", "incorrect"])
def login(request):
    login_deets = ["","",""]
    if request.param == "correct":
        login_deets = ["nc11@iitbbs.ac.in","namanbrowserstack","right"]
    elif request.param == "incorrect":
        login_deets = ["bj20151@astra.xlri.ac.in","namanbrdgffghowserstack","wrong"]
    return login_deets


def test_example(driver,login):
    # for login_i in login_list:
    browser_i = driver.name
    login_deets = login
    login_i = login[2]

    test_email = login_deets[0]
    test_password = login_deets[1]

    driver.get('https://www.browserstack.com/users/sign_in')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'user_email_login')))
    # Enter your login credentials and click the login button
    driver.find_element("id", "user_email_login").send_keys(test_email)
    # find password input field and insert password as well
    driver.find_element("id", "user_password").send_keys(test_password)
    # click login button
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'commit')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    WebDriverWait(driver, 5)

    live_dashboard_url = 'https://live.browserstack.com'
    if live_dashboard_url not in driver.current_url:
        driver.get(live_dashboard_url)

    if live_dashboard_url in driver.current_url:
        print('\nPass: Login for ',login_i," in ",browser_i,'\n')

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="platform-list-react"]/div/div[1]/div/div[4]/div[1]/div')))
        element.click()
        # print('Window click done')
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="platform-list-react"]/div/div[2]/div/div[2]/div[4]/div[1]/div[6]/div/div')))
        element.click()
        # print('edge click done')

        print('Pass: Dashboard for ',login_i," in ",browser_i,'\n')

    else:
        print('\nFail: Login for ',login_i," in ",browser_i,'\n')






















# from browserstack.local import Local
# from selenium import webdriver
# import pytest
# from selenium.webdriver.common.by import By

# def test_example(selenium):
#     selenium.get('https://bstackdemo.com/')

#     # locating product on webpage and getting name of the product
#     productText = selenium.find_element(By.XPATH, '//*[@id="1"]/p').text

#     # clicking the 'Add to cart' button
#     selenium.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

#     # waiting until the Cart pane has been displayed on the webpage
#     selenium.find_element(By.CLASS_NAME, 'float-cart__content')

#     # locating product in cart and getting name of the product in cart
#     productCartText = selenium.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

#     # checking whether product has been added to cart by comparing product name and marking test pass or fail
#     if productText == productCartText:
#         selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
#     else:
#         selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Product added to the cart not same as selected"}}')
