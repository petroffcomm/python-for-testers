
from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//input[@name='selected[]'])[1]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def set_dropdownlist_item(self, dlist_name, value_to_set):
        wd = self.app.wd
        if value_to_set is not None:
            Select(wd.find_element_by_name(dlist_name)).select_by_visible_text(value_to_set)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.primary_address)
        self.change_field_value("home", contact.primary_address_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_home)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        self.set_dropdownlist_item("bday", contact.birthday_day)
        self.set_dropdownlist_item("bmonth", contact.birthday_month)
        self.change_field_value("byear", contact.birthday_year)
        self.set_dropdownlist_item("aday", contact.anniversary_day)
        self.set_dropdownlist_item("amonth", contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondary_address_phone)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd

        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)

        # submit contact creation
        wd.find_element_by_xpath(".//input[@name='submit'][@value='Enter']").click()

        # return to home page
        self.app.navigation.go_to_home_page()

    def edit_first_contact(self, new_params):
        wd = self.app.wd
        self.app.navigation.open_home_page()

        # init modification process for first item table
        wd.find_element_by_xpath("(.//*[@id='maintable']//img[@alt='Edit'])[1]").click()
        self.fill_contact_form(new_params)
        # confirm modification
        wd.find_element_by_xpath("(.//input[@value='Update'])[2]").click()

        # return to home page
        self.app.navigation.go_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()

        self.select_first_contact()
        # init deletion process
        wd.find_element_by_xpath(".//input[@type='button'][@onclick='DeleteSel()']").click()
        # confirm deletion on popup window
        wd.switch_to_alert().accept()

        # return to home page
        self.app.navigation.go_to_home_page()

    def is_any_contact_exists(self):
        """ returns True if at least 1 contact is displayed """
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]")) != 0
