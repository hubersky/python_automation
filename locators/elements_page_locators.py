from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form_fields
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.XPATH, "//input[@type='email']")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created_form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p[id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    LIST_OF_NAME_BOX = (By.CSS_SELECTOR, "span[class='rct-title']")
    TEXT_ALERT = (By.CSS_SELECTOR, "span[class='text-success']")
    ITEM_CHECK = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIOBUTTON = (By.XPATH, "//label[@for='noRadio']")
    TEXT_ALERT = (By.XPATH, "//span[@class='text-success']")


class WebTablesLocators:
    # form_fields
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")

    ADD_BUTTON = (By.ID, "addNewRecordButton")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    EDIT_BUTTON = (By.XPATH, "//span[@title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#searchBox")

    # table_person
    ADD_PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    ROW = ".//ancestor::div[@class='rt-tr-group']"
    ALERT_NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    SELECT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

