import time

from pages.elements_page import *


class TestTextBox:

    def test(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        full_name, email, current_address, permanent_address = \
            text_box_page.fill_all_field()
        output_name, output_email, output_curr_addr, output_per_addr = \
            text_box_page.check_filled_form()
        assert full_name.replace("\n", " ") == output_name
        assert email.replace("\n", " ") == output_email
        assert current_address.replace("\n", " ") == output_curr_addr
        assert permanent_address.replace("\n", " ") == output_per_addr


class TestCheckBox:

    def test(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        select_item = check_box_page.get_checked_checkbox()
        alert_item = check_box_page.get_text_alert()
        assert select_item == alert_item


class TestRadioButton:

    def test(self, driver):
        radio_button_page = RadioButtonPage(driver,
                                            "https://demoqa.com/radio-button")
        radio_button_page.open()

        radio_button_page.click_on_radiobutton('yes')
        alert_yes = radio_button_page.get_text_alert()
        radio_button_page.click_on_radiobutton('impressive')
        alert_impressive = radio_button_page.get_text_alert()
        radio_button_page.click_on_radiobutton('no')
        alert_no = radio_button_page.get_text_alert()
        assert alert_yes == 'Yes'
        assert alert_impressive == 'Impressive'
        assert alert_no != 'No'


class TestWebTables:

    def test_add_person(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()

        new_person = web_tables_page.add_new_person()
        table_result = web_tables_page.check_add_person()
        assert new_person in table_result

    def test_search_person(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()

        key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
        web_tables_page.search_some_person(key_word)
        table_row = web_tables_page.check_search_person()
        assert key_word in table_row, "Person not found!"

    def test_edit_person_info(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()

        key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
        web_tables_page.search_some_person(key_word)
        edit_value = web_tables_page.edit_person_info()
        table_row = web_tables_page.check_search_person()
        assert edit_value in table_row

    def test_delete_person(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()

        email = web_tables_page.add_new_person()[3]
        web_tables_page.search_some_person(email)
        web_tables_page.delete_person()
        text = web_tables_page.check_delete_person()
        assert text == "No rows found"

    def test_change_count_row(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()

        count_rows = [5, 10, 20, 25, 50, 100]
        result = web_tables_page.select_table_row()
        assert result == count_rows


class TestButtonsPage:

    def test_buttons_page(self, driver):
        buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
        buttons_page.open()
        double = buttons_page.click_on_different_button('double')
        right = buttons_page.click_on_different_button('right')
        click = buttons_page.click_on_different_button('click')
        assert 'You have done a double click' == double
        assert 'You have done a right click' == right
        assert 'You have done a dynamic click' == click
