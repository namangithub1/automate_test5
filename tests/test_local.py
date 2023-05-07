import pytest
from browserstack.local import Local
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def login(request):
    login_deets = ["","",""]
    if request == "correct":
        login_deets = ["nc11@iitbbs.ac.in","namanbrowserstack","right"]
    elif request == "incorrect":
        login_deets = ["bj20151@astra.xlri.ac.in","namanbrdgffghowserstack","wrong"]
    return login_deets



def test_local(driver):
  # for login_i in login_list:
  login_i = "correct"
  browser_i = "chrome"
  login_deets = login(login_i)

  test_email = login_deets[0]
  test_password = login_deets[1]

  get_url = driver.current_url

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

  print("\n*****************Test: ",login_i," login, in browser: ",browser_i,"*****************")
  # Check if the login was successful by looking for the user avatar element
  try:
      WebDriverWait(driver, 20).until(EC.url_changes(('https://www.browserstack.com/users/sign_in')))
      live_dashboard_url = 'https://live.browserstack.com'
      driver.get(live_dashboard_url)
      assert live_dashboard_url in driver.current_url
      print('\nPass: Login\n')
      try:
          element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="platform-list-react"]/div/div[1]/div/div[4]/div[1]/div')))
          element.click()
          # print('Window click done')
          element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="platform-list-react"]/div/div[2]/div/div[2]/div[1]/div[1]/div[6]/div/div')))
          element.click()
          # print('edge click done')

          print('Pass: Dashboard\n')
      except:
          print('Fail: Dashboard\n')
          # driver.quit()
  except AssertionError:
      print('\nFail: Login\n')
      # driver.quit()
  # except TimeoutError as terr:
  #     print('\nFail: Login: ', driver.name, 'for cretentials:',login[2],"\n")
  except:
      # print('\nFail: Login: ', driver.name,"for cretentials:",login[2],"due to unknown reason\n")
      print('\nFail: Login (unkown reason)\n')
      # driver.quit()
  # driver.quit()