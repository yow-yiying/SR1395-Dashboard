from selenium.webdriver.common.by import By


class MainPageLocators(object):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")
    MY_TASKS_BUTTON = (By.XPATH, "//span[text()='My Tasks']")
    MY_DASHBOARD_TAB = (By.ID, "myDashboard")
    PRACTICE_STANDARDS_TAB = (By.XPATH, "//span[text()='PRACTICE STANDARDS']")


class DashboardPageLocators(object):
    CASE_LINKS = (
        By.XPATH, "//span[@data-title='Cases']/span[contains(text(), 'cases')]")


class ResultPageLocators(object):
    RESULT_PS = (
        By.XPATH, "//app-selected-practice-standard/div/div/div/div/div/div[1]")
    SEARCH_BAR = (By.XPATH, "//input[@type='search']")
