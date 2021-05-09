import pytest
import time
from unittest import TestCase
from pyexpect import expect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
driver.get("https://formy-project.herokuapp.com/form")
driver.maximize_window()
action = ActionChains(driver)
infoDict = {
    "FirstName": "Cristian",
    "LastName": "Barbu",
    "JobTitle": "Engineer"
}
firstName = driver.find_element_by_id("first-name")
lastName = driver.find_element_by_id("last-name")
jobTitle = driver.find_element_by_id("job-title")
firstName.send_keys(infoDict["FirstName"])
lastName.send_keys(infoDict["LastName"])
jobTitle.send_keys(infoDict["JobTitle"])
driver.find_element_by_id("radio-button-3").click()
driver.find_element_by_id("checkbox-1").click()
driver.find_element_by_id("select-menu").click()
driver.find_element_by_xpath("/html/body/div/form/div/div[6]/select/option[2]").click()
driver.find_element_by_id("datepicker").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[3]/td[4]").click()
driver.find_element_by_xpath("/html/body/div/form/div/div[8]/a").click()
alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alert")))
assert alert.text == "The form was successfully submitted!"
driver.quit()







