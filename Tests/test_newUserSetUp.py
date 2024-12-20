# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class TestNewUserSetUp():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
        #self.driver=webdriver.Edge()

    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(1280, 672)
    self.driver.find_element(By.ID, "username").send_keys("MarkLeo")
    self.driver.find_element(By.ID, "password").send_keys("123123")
    self.driver.find_element(By.CSS_SELECTOR, "[data-test=\"signin-submit\"]").click()

    self.vars = {}
  
  def teardown_method(self, method):
    
    self.driver.quit()
  
  def test_CheckTheBankAccountDetilasAsRequist(self):
    #Check if the account details are appeared as required
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"user-onboarding-next\"]").click()
    bank_name_input = self.driver.find_element(By.ID, "bankaccount-bankName-input")
    routing_number_input = self.driver.find_element(By.ID, "bankaccount-routingNumber-input")
    account_number_input = self.driver.find_element(By.ID, "bankaccount-accountNumber-input")
    time.sleep(1)

    # Assert that the validation message is displayed for each input
    assert bank_name_input.get_attribute("validationMessage") == "Please fill out this field.", \
        "Bank Name validation message is missing."
    assert routing_number_input.get_attribute("validationMessage") == "Please fill out this field.", \
        "Routing Number validation message is missing."
    assert account_number_input.get_attribute("validationMessage") == "Please fill out this field.", \
        "Account Number validation message is missing."

    print("Validation messages appeared correctly for all required fields.")
  
  def test_getStartedMessage(self):
    #Chick if the <h2> element with the "Get Started with Real World App" text appears on the homepage
    homepage_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-test=\"user-onboarding-dialog-title\"]"))
    )
    
    #assert self.driver.find_element(By.CSS_SELECTOR,"h2[data-test=\"user-onboarding-dialog-title\"]").text == "Get Started with Real World App"
    time.sleep(3)
  def test_startwithoutEnterBankAcoountDetilas(self):
   
    #self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"user-onboarding-next\"]").click()
     # Wait for the "Next" button to be clickable
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button'))
    )

    # Click the "Next" button
    next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button')
    next_button.click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDialog-container")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"bankaccount-submit\"]").click()
    time.sleep(2)
    #TO DO:
    #Chich if the button is disabled  

  #EMPTY FILED
  def test_BankNameIsEmpty(self):
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button'))
    )

    # Click the "Next" button
    next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button')
    next_button.click()

    # Fill out the form with an empty Bank Name
    self.driver.find_element(By.ID, "bankaccount-bankName-input").send_keys("")
    self.driver.find_element(By.ID, "bankaccount-routingNumber-input").send_keys("996645387")
    self.driver.find_element(By.ID, "bankaccount-accountNumber-input").send_keys("7774132232")

    # Wait for a moment to allow UI validation to occur (if needed)
    time.sleep(1)

    # Locate the "Save" button
    save_button = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='bankaccount-submit']")

    # Check if the "Save" button is disabled
    is_disabled = save_button.get_attribute("disabled")
    assert is_disabled == "true" or is_disabled == "", "The Save button is not disabled when it should be."

    print("Test passed: 'Save' button is correctly disabled when Bank Name is empty.")

  def test_RouterNumberIsEmpty(self):
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button'))
    )

    # Click the "Next" button
    next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button')
    next_button.click()

    # Fill out the form with an empty Bank Name
    self.driver.find_element(By.ID, "bankaccount-bankName-input").send_keys("Waters, King and O'Reilly Bank")
    self.driver.find_element(By.ID, "bankaccount-routingNumber-input").send_keys("")
    self.driver.find_element(By.ID, "bankaccount-accountNumber-input").send_keys("7774132232")

    # Wait for a moment to allow UI validation to occur (if needed)
    time.sleep(1)

    # Locate the "Save" button
    save_button = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='bankaccount-submit']")

    # Check if the "Save" button is disabled
    is_disabled = save_button.get_attribute("disabled")
    assert is_disabled == "true" or is_disabled == "", "The Save button is not disabled when it should be."

    print("Test passed: 'Save' button is correctly disabled when Router Number is empty.")


  #Result : this test must FAIL becuse the router number is empty
  def test_AccountNumberIsEmpty(self):
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button'))
    )

    # Click the "Next" button
    next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/button')
    next_button.click()

    # Fill out the form with an empty Bank Name
    self.driver.find_element(By.ID, "bankaccount-bankName-input").send_keys("Waters, King and O'Reilly Bank")
    self.driver.find_element(By.ID, "bankaccount-routingNumber-input").send_keys("7774132232")
    self.driver.find_element(By.ID, "bankaccount-accountNumber-input").send_keys("")

    # Wait for a moment to allow UI validation to occur (if needed)
    time.sleep(1)

    # Locate the "Save" button
    save_button = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='bankaccount-submit']")

    # Check if the "Save" button is disabled
    is_disabled = save_button.get_attribute("disabled")
    assert is_disabled == "true" or is_disabled == "", "The Save button is not disabled when it should be."

    print("Test passed: 'Save' button is correctly disabled when Account Number is empty.")


  
  
  #WRONG DATA
  
  def test_BankNameIsWrong(self):
    pass
  
   #Result : this test must FAIL becuse the Account number is wrong
  def test_AccountNumberIsWrong(self):
    pass

  #Result : this test must FAIL becuse the router number is wrong
  def test_RouterNumberIsWrong(self):
    pass
