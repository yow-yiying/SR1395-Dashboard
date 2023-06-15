import enquiry.constants as const
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import string
import random


class Enquiry(webdriver.Chrome):
    def __init__(self):
        super(Enquiry, self).__init__()
        self.implicitly_wait(8)
        self.maximize_window()

    def land_ssnet_login(self, env="dev"):
        if env == "dev":
            self.get(const.DEV_URL)
        elif env == "sit":
            self.get(const.SIT_URL)

    def login(self, username="fsccaseworker"):

        login_username = self.find_element(By.ID, "username")
        login_username.send_keys(username)

        login_password = self.find_element(By.ID, "password")
        login_password.send_keys(username + "_password")

        login_button = self.find_element(By.TAG_NAME, "button")
        login_button.click()

    def create_new_enquiry(self,
                           input_channel_of_enquiry="Telephone",
                           input_enquiry_details="testing testing",
                           input_duration_of_contact=55,
                           input_date_of_referral=const.TODAY,
                           input_source_of_referral="Community - Schools",
                           input_date_of_ack=const.TODAY,
                           input_immediate_assist="No",
                           ):

        new_button = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='NEW']")))
        time.sleep(2)
        new_button.click()
        create_enquiry = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "CREATE ENQUIRY"))
        )
        create_enquiry.click()

        # Channel of Enquiry
        channel_of_enquiry = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='channel']")))
        channel_of_enquiry.click()
        selected_channel_of_enquiry = self.find_element(
            By.XPATH, f"//div[@role='option' and .//*[text()='{input_channel_of_enquiry}']]")
        selected_channel_of_enquiry.click()

        # Enquiry Details
        enquiry_details = self.find_element(
            By.XPATH, "//textarea[@formcontrolname='details']")
        enquiry_details.send_keys(f"{input_enquiry_details}")

        # Duration of Contact
        duration_of_contact = self.find_element(
            By.XPATH, "//input[@formcontrolname='duration']")
        duration_of_contact.send_keys(f"{input_duration_of_contact}")

        # Date of Referral
        date_of_referral = self.find_element(By.XPATH, "//app-datepicker[@formcontrolname='referralDate']/" +
                                             "mat-form-field/div/div/div/input[1]")
        date_of_referral.send_keys(f"{input_date_of_referral}")

        # Source of Referral
        source_of_referral = self.find_element(
            By.XPATH, "//ng-select[@formcontrolname='referralSource']")
        source_of_referral.click()
        selected_source_of_referral = self.find_element(By.XPATH, "//ng-select[@formcontrolname='referralSource']/ng-dropdown-panel/"
                                                        + f"div/div/div/span[text()='{input_source_of_referral}']")
        selected_source_of_referral.click()

        # Date of Referral Acknowledgement
        date_of_referral_acknowledgement = self.find_element(By.XPATH, "//app-datepicker[@formcontrolname='dateOfReferralAcknowledgement']/" +
                                                             "mat-form-field/div/div/div/input[1]")
        date_of_referral_acknowledgement.send_keys(f"{input_date_of_ack}")

        # Immediate assistance?
        radio_buttons = self.find_elements(
            By.XPATH, '//input[@formcontrolname="immediateAttention"]')

        if input_immediate_assist == "Yes":
            radio_buttons[0].click()
        elif input_immediate_assist == "No":
            radio_buttons[1].click()

    def fill_enquiry_outcome(self,
                             hasOutcome=False,
                             input_outcome_for_enquiry="Information given",
                             input_date_of_outcome=const.TODAY,
                             input_updated_ref_source_date=const.TODAY
                             ):
        if hasOutcome:
            # Enquiry Outcome Checkbox
            outcome_checkbox = self.find_element(
                By.XPATH, "//label[text()=' Client has an Enquiry Outcome ']")
            outcome_checkbox.click()

            # Outcome For Enquiry
            outcome_for_enquiry = self.find_element(
                By.XPATH, "//ng-select[@formcontrolname='outcome']")
            outcome_for_enquiry.click()
            selected_outcome_for_enquiry = self.find_element(By.XPATH, "//ng-select[@formcontrolname='outcome']/ng-dropdown-panel/"
                                                             + f"div/div/div/span[text()='{input_outcome_for_enquiry}']")
            selected_outcome_for_enquiry.click()

            # Date of Outcome
            date_of_outcome = self.find_element(By.XPATH, "//app-datepicker[@formcontrolname='outcomeDate']/" +
                                                "mat-form-field/div/div/div/input[1]")
            date_of_outcome.send_keys(f"{input_date_of_outcome}")

            # Updated Referring Source Date
            date_of_updated_ref_source = self.find_element(By.XPATH, "//app-datepicker[@formcontrolname='updatedReferralSourceDate']/" +
                                                           "mat-form-field/div/div/div/input[1]")
            date_of_updated_ref_source.send_keys(
                f"{input_updated_ref_source_date}")

    def search_nric(self, input_nric):

        # Search NRIC
        search_nric = self.find_element(
            By.XPATH, f"//input[@formcontrolname='userId']")
        search_nric.send_keys(f"{input_nric}")
        search_button = self.find_element(
            By.XPATH, "//button[text()=' SEARCH ']")
        search_button.click()

        # Proceed button
        try:
            proceed_button = self.find_element(
                By.XPATH, "//button[text()=' Proceed ']")
            proceed_button.click()
        except:
            # if no "Proceed" popup appears, need to register NRIC as new person

            # ID Type
            id_type = self.find_element(
                By.XPATH, "//ng-select[@formcontrolname='idType']")
            id_type.click()
            selected_id_type = self.find_element(By.XPATH, "//ng-select[@formcontrolname='idType']/ng-dropdown-panel/"
                                                 + "div/div/div/span[text()='Singapore Pink Identification Card']")
            selected_id_type.click()

            # Citizenship Status
            citizenship = self.find_element(
                By.XPATH, "//ng-select[@formcontrolname='citizenship']")
            citizenship.click()
            selected_citizenship = self.find_element(By.XPATH, "//ng-select[@formcontrolname='citizenship']/ng-dropdown-panel/"
                                                     + "div/div/div/span[text()='Singapore Citizen']")
            selected_citizenship.click()

            # Name
            name = self.find_element(
                By.XPATH, "//input[@formcontrolname='name']")
            random_string = ''.join(random.choice(
                string.ascii_uppercase) for _ in range(3))
            name.send_keys("SR1395 Test Person " + random_string)

            # Language Spoken
            language_spoken = self.find_element(
                By.XPATH, "//ng-select[@formcontrolname='code']")
            language_spoken.click()
            selected_language_spoken = self.find_element(By.XPATH, "//ng-select[@formcontrolname='code']/ng-dropdown-panel/"
                                                         + "div/div/div/span[text()='English']")
            selected_language_spoken.click()

            # Ethnicity
            ethnicity = self.find_element(
                By.XPATH, "//ng-select[@formcontrolname='ethnicity']")
            ethnicity.click()
            selected_ethnicity = self.find_element(By.XPATH, "//ng-select[@formcontrolname='ethnicity']/ng-dropdown-panel/"
                                                   + "div/div/div/span[text()='Chinese']")
            selected_ethnicity.click()

            # Date of Birth
            date_of_birth = self.find_element(
                By.XPATH, "//app-datepicker[@formcontrolname='dob']/" +
                "mat-form-field/div/div/div/div/input[1]")
            date_of_birth.send_keys("01/01/1999")

            # Gender
            gender = self.find_element(
                By.XPATH, "//ng-select[@formcontrolname='gender']")
            gender.click()
            selected_gender = self.find_element(By.XPATH, "//ng-select[@formcontrolname='gender']/ng-dropdown-panel/"
                                                + "div/div/div/span[text()='Male']")
            selected_gender.click()

            # Postal Code
            postal_code = self.find_element(
                By.XPATH, "//app-address-form//input[@formcontrolname='postal']")
            postal_code.send_keys(765432)
            postal_code.send_keys(Keys.TAB)

            time.sleep(2)

            # Block / House No.
            block_no = self.find_element(
                By.XPATH, "//app-address-form//input[@formcontrolname='blkno']")
            block_no.send_keys("432")

            # Street Name
            street = self.find_element(
                By.XPATH, "//app-address-form//input[@formcontrolname='street']")
            street.send_keys("Test Street")

            # Save address
            save_address = self.find_element(
                By.XPATH, "//app-address-form//button[text()='OK ']")
            save_address.click()

    def save_enquiry(self):
        save_button = self.find_element(By.XPATH, "//button[text()=' SAVE ']")
        save_button.click()

    def print_success_msg(self):
        success_msg = self.find_element(
            By.XPATH, "//div[contains(text(), 'You have successfully submitted')]")
        print(success_msg.text)
