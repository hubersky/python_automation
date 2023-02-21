import random

from generator.generator import generated_person
from locators.elements_page_locators import *
from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_field(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME) \
            .send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL) \
            .send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS) \
            .send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS) \
            .send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(
            self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(
            self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.LIST_OF_NAME_BOX)
        count = 17
        while count != 0:
            item = item_list[random.randint(0, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkbox(self):
        check_list = self.elements_are_present(self.locators.ITEM_CHECK)
        data = []
        for box in check_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '') \
            .replace('.', '').lower()

    def get_text_alert(self):
        alert_text_list = self.elements_are_visible(self.locators.TEXT_ALERT)
        data = []
        for item in alert_text_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radiobutton(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_text_alert(self):
        return self.element_is_present(self.locators.TEXT_ALERT).text


class WebTablesPage(BasePage):
    locators = WebTablesLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            count -= 1
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME) \
                .send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME) \
                .send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL) \
                .send_keys(email)
            self.element_is_visible(self.locators.AGE) \
                .send_keys(age)
            self.element_is_visible(self.locators.SALARY) \
                .send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT) \
                .send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return [first_name, last_name, str(age), email, str(salary),
                    department]

    def check_add_person(self):
        person_list = self.elements_are_present(self.locators.ADD_PERSON_LIST)
        data = []

        for i in person_list:
            data.append(i.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW)
        return row.text.splitlines()

    def edit_person_info(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        choose_field = random.randint(0, 5)
        if choose_field == 0:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME) \
                .send_keys(first_name)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return first_name
        if choose_field == 1:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.LAST_NAME).clear()
            self.element_is_visible(self.locators.LAST_NAME) \
                .send_keys(last_name)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return last_name
        if choose_field == 2:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.EMAIL).clear()
            self.element_is_visible(self.locators.EMAIL) \
                .send_keys(email)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return email
        if choose_field == 3:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.AGE).clear()
            self.element_is_visible(self.locators.AGE) \
                .send_keys(age)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(age)
        if choose_field == 4:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.SALARY).clear()
            self.element_is_visible(self.locators.SALARY) \
                .send_keys(salary)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(salary)
        if choose_field == 5:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.DEPARTMENT).clear()
            self.element_is_visible(self.locators.DEPARTMENT) \
                .send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return department
