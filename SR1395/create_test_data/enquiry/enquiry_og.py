from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime, timedelta

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# <---- CONSTANTS ---->
driver = webdriver.Chrome()
today = time.strftime("%d/%m/%Y")

# <---- OPEN WEBSITE ---->
# driver.get("https://dev.one.ssnet.gov.sg/mockServer/mock-ad.html")  # Dev
driver.get("https://sit.one.ssnet.gov.sg/mockServer/mock-ad.html")  # SIT

# <---- LOGIN ---->
login_username = driver.find_element(By.ID, "username")
login_username.send_keys("fsccaseworker")

login_password = driver.find_element(By.ID, "password")
login_password.send_keys("fsccaseworker_password")

login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

# <---- CREATE NEW ENQUIRY ---->
# Wait for page to load and create new enquiry
new_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='main-click-trigger ng-tns-c213-1' and .//*[text()='NEW']]"))
)
time.sleep(2)
new_button.click()
create_enquiry = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "CREATE ENQUIRY"))
)
create_enquiry.click()

# <---- DEFINE ENQUIRY INPUTS ---->
# 1. Enquiry
input_channel_of_enquiry = "Telephone"
input_enquiry_details = "SIT Test 10.5"  # <-- update for each test case
input_duration_of_contact = 55

# 1. Enquiry - Referral Agency
input_date_of_referral = "01/05/2023"  # <-- update for each test case

# due_date = (datetime.strptime(input_date_of_referral, "%d/%m/%Y")
#             + timedelta(days=14)).strftime("%d/%m/%Y")
# print(due_date)

# Community - Schools
# Community - Family / Friends
# Self-Referral
# <-- update for each test case
input_source_of_referral = "Community - Schools"
input_date_of_ack = "30/05/2023"  # <-- update for each test case
input_immediate_assist = 1  # 0 for Yes, 1 for No

# 1. Enquiry - Enquiry Outcome
hasOutcome = True  # <-- update to True for enquiry outcome, else False
input_outcome_for_enquiry = "New Intake"
input_date_of_outcome = today
input_updated_ref_source_date = today

# 2. Person Information
# Person 1: S0999708C
# Person 2: S2399802E
# Person 3: S5822104Z
input_search_nric = "S0195085A"  # <-- update for each test case

# <---- FILLING IN ENQUIRY FORM ---->
# Channel of Enquiry
channel_of_enquiry = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//ng-select[@formcontrolname='channel']"))
)
channel_of_enquiry.click()
selected_channel_of_enquiry = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//div[@role='option' and .//*[text()='{input_channel_of_enquiry}']]"))
)
selected_channel_of_enquiry.click()

# Enquiry Details
enquiry_details = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//textarea[@formcontrolname='details']"))
)
enquiry_details.send_keys(f"{input_enquiry_details}")

# Duration of Contact
duration_of_contact = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[@formcontrolname='duration']"))
)
duration_of_contact.send_keys(f"{input_duration_of_contact}")

# Date of Referral
date_of_referral = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//app-datepicker[@formcontrolname='referralDate']/" +
                                    "mat-form-field/div/div/div/input[1]"))
)
date_of_referral.send_keys(f"{input_date_of_referral}")

# Source of Referral
source_of_referral = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//ng-select[@formcontrolname='referralSource']"))
)
source_of_referral.click()
selected_source_of_referral = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='referralSource']/ng-dropdown-panel/"
                                + f"div/div/div/span[text()='{input_source_of_referral}']"))
)
selected_source_of_referral.click()

# Date of Referral Acknowledgement
date_of_referral_acknowledgement = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//app-datepicker[@formcontrolname='dateOfReferralAcknowledgement']/" +
                                    "mat-form-field/div/div/div/input[1]"))
)
date_of_referral_acknowledgement.send_keys(f"{input_date_of_ack}")

# Immediate assistance?
radio_buttons = driver.find_elements(
    By.XPATH, '//input[@formcontrolname="immediateAttention"]')
# print("radiobtns", len(radio_buttons))
radio_buttons[input_immediate_assist].click()

if hasOutcome:

    # Enquiry Outcome Checkbox
    outcome_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[text()=' Client has an Enquiry Outcome ']"))
    )
    outcome_checkbox.click()

    # Outcome For Enquiry
    outcome_for_enquiry = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//ng-select[@formcontrolname='outcome']"))
    )
    outcome_for_enquiry.click()
    selected_outcome_for_enquiry = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='outcome']/ng-dropdown-panel/"
                                    + f"div/div/div/span[text()='{input_outcome_for_enquiry}']"))
    )
    selected_outcome_for_enquiry.click()

    # Date of Outcome
    date_of_outcome = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//app-datepicker[@formcontrolname='outcomeDate']/" +
                                        "mat-form-field/div/div/div/input[1]"))
    )
    date_of_outcome.send_keys(f"{input_date_of_outcome}")

    # Updated Referring Source Date
    date_of_updated_ref_source = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//app-datepicker[@formcontrolname='updatedReferralSourceDate']/" +
                                        "mat-form-field/div/div/div/input[1]"))
    )
    date_of_updated_ref_source.send_keys(f"{input_updated_ref_source_date}")

    # Search NRIC
search_nric = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, f"//input[@formcontrolname='userId']"))
)
search_nric.send_keys(f"{input_search_nric}")
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()=' SEARCH ']"))
)
search_button.click()

# Proceed button
proceed_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()=' Proceed ']"))
)
proceed_button.click()


# <---- SAVING ENQUIRY ---->
save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()=' SAVE ']"))
)
save_button.click()

# driver.quit()

while (True):
    pass
