import time
import pytest
from unittest import TestCase
from pyexpect import expect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UITest(TestCase):
    def test_login(self):
        ''' 
        Test if I can login to website.
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://selenium-blog.herokuapp.com/login")
        driver.maximize_window()
        email = driver.find_element_by_xpath('//*[@id="session_email"]')
        email.send_keys('crs12@test.com')
        password = driver.find_element_by_xpath('//*[@id="session_password"]')
        password.send_keys('test123')
        logIn = driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/div/input')
        action = ActionChains(driver)
        action.click(logIn)
        action.perform()
        banner = driver.find_element_by_xpath('//*[@id="flash_success"]')
        str1 = banner.text
        expect(str1).to_equal("You have successfully logged in!")
        assert str1 == 'You have successfully logged in!'
    
    def test_keypress(self):
        '''
        Test if I can enter my name.
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/keypress")
        driver.maximize_window()
        name = driver.find_element_by_id('name')
        name.send_keys("Cristian Barbu")
    
    def test_autocomplete(self):
        '''
        Test autocomplete full address
        '''
        full_address = {"Address": "Bvd. Iuliu Maniu nr. 1-3, Camin Leu A",
                "Street1": "Iuliu Maniu",
                "Street2": "Moinesti",
                "City": "Bucuresti",
                "State": "Bucuresti",
                "Zipcode": 123456,
                "Country": "Romania"}

        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/autocomplete")
        driver.maximize_window()
        address = driver.find_element_by_id("autocomplete")
        street1 = driver.find_element_by_id("street_number")
        street2 = driver.find_element_by_id("route")
        city = driver.find_element_by_id("locality")
        state = driver.find_element_by_id("administrative_area_level_1")
        zipcode = driver.find_element_by_id("postal_code")
        country = driver.find_element_by_id("country")

        address.send_keys(full_address.get("Address"))
        street1.send_keys(full_address.get("Street1"))
        street2.send_keys(full_address.get("Street2"))
        city.send_keys(full_address.get("City"))
        state.send_keys(full_address.get("State"))
        zipcode.send_keys(full_address.get("Zipcode"))
        country.send_keys(full_address.get("Country"))

    def test_scroll(self):
        '''
        Test scroll page and complete bottom fields
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/scroll")
        driver.maximize_window()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 1000)")
        name = driver.find_element_by_id("name")
        name.send_keys("Cristian Barbu")
        date = driver.find_element_by_id("date")
        date.send_keys("03/29/2021")
    
    def test_dragndrop(self):
        '''
        Test if drag and drop action is succesfull
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/dragdrop")
        driver.maximize_window()
        image = driver.find_element_by_id("image")
        box =  driver.find_element_by_id("box")
        action = ActionChains(driver)
        action.drag_and_drop(image, box).perform()
        message = driver.find_element_by_xpath('//*[@id="box"]/p')
        assert message.text == "Dropped!"
    
    def test_radioButtons(self):
        '''
        Test radio buttons selections
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/radiobutton")
        driver.maximize_window()
        action = ActionChains(driver)
        radioButton1 = driver.find_element_by_xpath("/html/body/div/div[1]/input")
        action.click(radioButton1).perform()
        radioButton2 = driver.find_element_by_xpath("/html/body/div/div[2]/input")
        action.click(radioButton2).perform()
        radioButton3 = driver.find_element_by_xpath("/html/body/div/div[3]/input")
        action.click(radioButton3).perform()
    
    def test_datePicker(self):
        '''
        Test date selection
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/datepicker")
        driver.maximize_window()
        action = ActionChains(driver)
        dateField = driver.find_element_by_id("datepicker")
        action.click(dateField).perform()
        date = driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[3]/td[4]")
        action.click(date).perform()

    def test_form(self):
        '''
        Test form completion with all the types
        '''
        driver = webdriver.Chrome(r'C:\Users\cristian.barbu1212\Downloads\chromedriver')
        driver.get("https://formy-project.herokuapp.com/form")
        driver.maximize_window()

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