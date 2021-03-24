#selenium dependent imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

#system time if we need to pause stuff
import time
import datetime

####################
#Input field values#
#Edit as needed#####
####################
accountName = "ChidoTest__" + str(datetime.date.today())
firstName = "ChidoTest"
lastName = "LastTest"
Email = "ChidoTest@Test.com"
DayPh = "1231231231"
NightPh = "1231231231"
BDay = "11111990"
SocSecNum = "111222333"
AddLine_1 = "Test Suite Ave 123rd"
AddLine_2 = ""
Zip_9 = "972661234"
City = "Portland"
Zip_5 = "97266"
bankName = "BigBank"
bankAccName = "NoMoney"
accountNumber = "123456789"
routingNumber = "325070760"

####################
#Business Info######
####################
businessName = "CorSourceTesting"
empIdNum = "111222333"
businessEmail = "corsourcetesting@gmail.com"
businessPh = "1234567891"


# Init chromium driver // and clear cache
driver = webdriver.Chrome("C:\\Users\\ChidoNguyen\\Documents\\chromedriver")
targetURL = ('C:\\Users\\ChidoNguyen\\Documents\\PythonAutomate\\MSUG\\MSUG.html')
#driver.get(targetURL)

class TestMSUGclass(unittest.TestCase):
        
    def setUp(self):
        driver.get(targetURL)
        
    def test_personal_MSUG_Form_Element_And_Input(self):
        try:
            (driver.find_element_by_id("accountName")).send_keys(accountName)
            time.sleep(2)
        except NoSuchElementException:
            print("Failed to find/input Account Name")
            raise
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/form/div[2]/div/div/div/button").click()
            driver.find_element_by_link_text("Personal").click()
        except NoSuchElementException:
            print("Failed to drop and select Personal Acccount")
            raise
        
        try:
            driver.find_element_by_id("firstName").send_keys(firstName + "_Personal")
            driver.find_element_by_id("lastName").send_keys(lastName)
            driver.find_element_by_id("email").send_keys(Email)
            driver.find_element_by_id("dayPhone").send_keys(DayPh)
            driver.find_element_by_id("eveningPhone").send_keys(NightPh)
            driver.find_element_by_id("birthDate").send_keys(BDay)
            driver.find_element_by_id("ssn").send_keys(SocSecNum)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div[1]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Personal Information details")
            raise
        
        try:
            driver.find_element_by_id("line11").send_keys(AddLine_1)
            driver.find_element_by_id("line21").send_keys(AddLine_2)
            driver.find_element_by_id("city1").send_keys(City)
            #create select object for drop down menuts
            dropCountry =  Select(driver.find_element_by_id("country11"))
            dropCountry.select_by_visible_text("USA")
            dropState = Select(driver.find_element_by_id("state-select1"))
            dropState.select_by_visible_text("Oregon")
            driver.find_element_by_id("zip1").send_keys(Zip_5)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div[2]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Personal Address details")
            raise
        
        try:
            driver.find_element_by_id("bankName1").send_keys(bankName)
            driver.find_element_by_id("bankAccount1").send_keys(bankAccName)
            dropAccOwn = Select(driver.find_element_by_id("changeOwnership1"))
            dropAccOwn.select_by_index(1)
            dropAccType = Select(driver.find_element_by_id("changeAccountType1"))
            dropAccType.select_by_index(1)
            driver.find_element_by_id("accountNumber1").send_keys(accountNumber)
            driver.find_element_by_id("routingNumber1").send_keys(routingNumber)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div[3]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Bank Information details")
            raise
        
        try:
            driver.find_element_by_id("condition").click()
            driver.find_element_by_id("signature").send_keys("DigitalSignature")
        except NoSuchElementException:
            print("Failed to confirm TC and signing of Digital Signature")
            raise
        
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/button[2]").click()
            time.sleep(10)
        except NoSuchElementException:
            print("Failed to submit sign-up form.")
            raise
        
        try:
            self.assertTrue(driver.find_element_by_xpath("/html/body/div[2]/div/div/div").is_displayed(), True)
        except :
            print("Submission failure")
            raise
    
    
    def test_business_Form_Element_And_Input(self):
        try:
            (driver.find_element_by_id("accountName")).send_keys(accountName + "_BUSINESS")
            time.sleep(2)
        except NoSuchElementException:
            print("Failed to find/input Account Name")
            raise
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/form/div[2]/div/div/div/button").click()
            driver.find_element_by_link_text("Business").click()
        except NoSuchElementException:
            print("Failed to drop and select Business Acccount")
            raise
        
        try:
            driver.find_element_by_id("firstName2").send_keys(firstName)
            driver.find_element_by_id("lastName2").send_keys(lastName)
            driver.find_element_by_id("email2").send_keys(Email)
            driver.find_element_by_id("dayPhone2").send_keys(DayPh)
            driver.find_element_by_id("eveningPhone2").send_keys(NightPh)
            driver.find_element_by_id("birthDate2").send_keys(BDay)
            driver.find_element_by_id("ssn2").send_keys(SocSecNum)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Personal Information details")
            raise
        
        try:
            driver.find_element_by_id("line112").send_keys(AddLine_1)
            driver.find_element_by_id("line212").send_keys(AddLine_2)
            driver.find_element_by_id("city12").send_keys(City)
            #create select object for drop down menuts
            dropCountry =  Select(driver.find_element_by_id("country112"))
            dropCountry.select_by_visible_text("USA")
            dropState = Select(driver.find_element_by_id("state-select112"))
            dropState.select_by_visible_text("Oregon")
            driver.find_element_by_id("zip12").send_keys(Zip_5)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div[2]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Personal Address details")
            raise
        
        try:
            driver.find_element_by_id("businessName").send_keys(businessName)
            driver.find_element_by_id("ein").send_keys(empIdNum)
            driver.find_element_by_id("bemail").send_keys(businessEmail)
            driver.find_element_by_id("bphone").send_keys(businessPh)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to enter business information.")
            raise
        
        try:
            driver.find_element_by_id("line12").send_keys(AddLine_1)
            driver.find_element_by_id("line22").send_keys(AddLine_2)
            driver.find_element_by_id("city2").send_keys(City)
            #create select object for drop down menuts
            dropCountry =  Select(driver.find_element_by_id("country21"))
            dropCountry.select_by_visible_text("USA")
            dropState = Select(driver.find_element_by_id("state-select21"))
            dropState.select_by_visible_text("Oregon")
            driver.find_element_by_id("zip2").send_keys(Zip_9)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div[4]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Business Address details")
            raise
        
        try:
            driver.find_element_by_id("bankName2").send_keys(bankName)
            driver.find_element_by_id("bankAccount2").send_keys(bankAccName)
            dropAccOwn = Select(driver.find_element_by_id("changeOwnership2"))
            dropAccOwn.select_by_index(1)
            dropAccType = Select(driver.find_element_by_id("changeAccountType2"))
            dropAccType.select_by_index(1)
            driver.find_element_by_id("accountNumber2").send_keys(accountNumber)
            driver.find_element_by_id("routingNumber2").send_keys(routingNumber)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div[5]/div/button[2]").click()
        except NoSuchElementException:
            print("Failed to find and input Bank Information details")
            raise
        
        try:
            driver.find_element_by_id("condition").click()
            driver.find_element_by_id("signature").send_keys("DigitalSignature")
        except NoSuchElementException:
            print("Failed to confirm TC and signing of Digital Signature")
            raise
        
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/button[2]").click()
            # time.sleep(10)
        except NoSuchElementException:
            print("Failed to submit sign-up form.")
            raise
        
        try:
            time.sleep(10)
            self.assertTrue(driver.find_element_by_xpath("/html/body/div[2]/div/div/div").is_displayed(), True)
        except TimeoutException:
            print("Submission failure")
            raise


if __name__ == "__main__":
    unittest.main()
    driver.close()
