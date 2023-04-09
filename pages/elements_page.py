import random
import time

import requests
from selenium.common import TimeoutException

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
        list_info = [first_name, last_name, email, age, salary, department]
        list_locators = [self.locators.FIRST_NAME, self.locators.LAST_NAME,
                         self.locators.EMAIL, self.locators.AGE,
                         self.locators.SALARY, self.locators.DEPARTMENT]
        choose_field = random.randint(0, 5)
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(list_locators[choose_field]).clear()
        self.element_is_visible(list_locators[choose_field]) \
            .send_keys(list_info[choose_field])
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return list_info[choose_field]

    def delete_person(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    def check_delete_person(self):
        return self.element_is_present(self.locators.ALERT_NO_ROWS_FOUND).text

    def select_table_row(self):
        self.remove_footer()
        self.remove_fixed_ban()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            count_button = self.element_is_present(self.locators.SELECT_ROWS)
            self.go_to_element(count_button)
            count_button.click()
            self.element_is_visible(
                (By.CSS_SELECTOR, f'option[value="{i}"]')).click()
            data.append(self.count_rows())
        return data

    def count_rows(self):
        list_rows = self.elements_are_present(self.locators.ADD_PERSON_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        match type_click:
            case 'double':
                self.action_double_click(
                    self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
                return self.check_click_button(
                    self.locators.DOUBLE_CLICK_MESSAGE)
            case 'right':
                self.action_right_click(
                    self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
                return self.check_click_button(
                    self.locators.RIGHT_CLICK_MESSAGE)
            case 'click':
                self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
                return self.check_click_button(self.locators.CLICK_ME_MESSAGE)

    def check_click_button(self, locator):
        return self.element_is_present(locator).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_link(self):
        link = self.element_is_visible(self.locators.HOME_LINK)
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    def check_change_color(self):
        color_button = self.element_is_present(
            self.locators.COLOR_CHANGE_BUTTON)
        color_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_after = color_button.value_of_css_property('color')
        return color_before, color_after

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.WILL_ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_visible_after_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True
