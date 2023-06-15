from locators import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(8)
        # if self.driver.get_window_size()['width'] != driver.execute_script('return window.screen.availWidth') or \
        #         driver.get_window_size()['height'] != driver.execute_script('return window.screen.availHeight'):
        #     self.driver.maximize_window()
        self.original_window = self.driver.current_window_handle


class MainPage(BasePage):
    def navigate_to_dashboard(self):
        my_tasks_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.MY_TASKS_BUTTON)
        )
        time.sleep(3)
        my_tasks_button.click()
        my_dashboard_tab = self.driver.find_element(
            *MainPageLocators.MY_DASHBOARD_TAB)
        time.sleep(2)
        my_dashboard_tab.click()
        # try:
        #     element = WebDriverWait(self.driver, 2).until(
        #         EC.presence_of_element_located((By.LINK_TEXT, "lkskd"))
        #     )
        # except:
        #     print("false".encode('utf-8'))
        # print("yay")
        practice_standards_tab = self.driver.find_element(
            *MainPageLocators.PRACTICE_STANDARDS_TAB)
        practice_standards_tab.click()

    def login(self, username="fsccaseworker"):
        login_username = self.driver.find_element(
            *MainPageLocators.USERNAME_FIELD)
        login_username.send_keys(username)

        login_password = self.driver.find_element(
            *MainPageLocators.PASSWORD_FIELD)
        login_password.send_keys(username + "_password")

        login_button = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()


class DashboardPage(BasePage):
    def click_case_count(self, link_index=0):
        time.sleep(3)
        all_case_links = self.driver.find_elements(
            *DashboardPageLocators.CASE_LINKS)
        # for case in all_case_links:
        #     print("case", case.text)
        all_case_links[link_index].click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_window:
                self.driver.switch_to.window(window_handle)
                break


class ResultPage(BasePage):
    def is_practise_standard_matches(self, practice_standard):

        result_text = self.driver.find_element(
            *ResultPageLocators.RESULT_PS).text
        print(result_text.replace('\u200b', ''))
        return practice_standard in result_text

    def is_record_found(self, ref_no):
        search_bar = self.driver.find_element(*ResultPageLocators.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(ref_no)
        try:
            self.driver.implicitly_wait(0)
            element = self.driver.find_element(By.LINK_TEXT, ref_no)
        except:
            self.driver.implicitly_wait(8)
            return False
        self.driver.implicitly_wait(8)
        return True

        # elements = WebDriverWait(self.driver, 2).until(
        #     EC.presence_of_all_elements_located((By.LINK_TEXT, ref_no)))
        # elements = WebDriverWait(self.driver, 2).until(
        #     EC.presence_of_all_elements_located((By.LINK_TEXT, ref_no))
        # )
        elements = self.driver.find_elements(
            By.LINK_TEXT, ref_no)
        # print(elements)
        # for thing in elements:
        #     print("huh", thing.text)
        is_found = len(elements) != 0
        return is_found
