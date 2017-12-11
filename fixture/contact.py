import re
from selenium.webdriver.support.select import Select
from model.contact import Contact
from utils.data_transformations import set_none_or_value_of

class ContactHelper:
    def __init__(self, app):
        self.app = app

    contacts_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("(.//input[@name='selected[]'])")[index].click()

    def set_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_field_value(self, field_name):
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value")

    def set_dropdownlist_item(self, dlist_name, value_to_set):
        wd = self.app.wd
        if value_to_set is not None:
            Select(wd.find_element_by_name(dlist_name)).select_by_visible_text(value_to_set)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("(.//*[@id='maintable']//img[@alt='Edit'])")[index].click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("(.//*[@id='maintable']//img[@alt='Details'])")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.set_field_value("firstname", contact.fname)
        self.set_field_value("middlename", contact.mname)
        self.set_field_value("lastname", contact.lname)
        self.set_field_value("nickname", contact.nickname)
        self.set_field_value("title", contact.title)
        self.set_field_value("company", contact.company)
        self.set_field_value("address", contact.primary_address)
        self.set_field_value("home", contact.primary_phone)
        self.set_field_value("mobile", contact.mobile_phone)
        self.set_field_value("work", contact.work_phone)
        self.set_field_value("fax", contact.fax)
        self.set_field_value("email", contact.email_1)
        self.set_field_value("email2", contact.email_2)
        self.set_field_value("email3", contact.email_3)
        self.set_field_value("homepage", contact.homepage)
        self.set_dropdownlist_item("bday", contact.birthday_day)
        self.set_dropdownlist_item("bmonth", contact.birthday_month)
        self.set_field_value("byear", contact.birthday_year)
        self.set_dropdownlist_item("aday", contact.anniversary_day)
        self.set_dropdownlist_item("amonth", contact.anniversary_month)
        self.set_field_value("ayear", contact.anniversary_year)
        self.set_field_value("address2", contact.secondary_address)
        self.set_field_value("phone2", contact.secondary_phone)
        self.set_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd

        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)

        # submit contact creation
        wd.find_element_by_xpath(".//input[@name='submit'][@value='Enter']").click()

        # return to home page
        self.app.navigation.return_to_home_page()
        # reset records' cache
        self.contacts_cache = None

    def edit_first_contact(self, new_params):
        self.edit_contact_by_index(0, new_params)

    def edit_contact_by_index(self, index, new_params):
        wd = self.app.wd

        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_params)
        # confirm modification
        wd.find_element_by_xpath("(.//input[@value='Update'])[2]").click()

        # return to home page
        self.app.navigation.return_to_home_page()
        # reset records' cache
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()

        self.select_contact_by_index(index)
        # init deletion process
        wd.find_element_by_xpath(".//input[@type='button'][@onclick='DeleteSel()']").click()
        # confirm deletion on popup window
        wd.switch_to_alert().accept()

        # return to home page
        self.app.navigation.return_to_home_page()
        # reset records' cache
        self.contacts_cache = None

    def is_any_contact_exists(self):
        """ returns True if at least 1 contact is displayed """
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]")) != 0

    def count(self):
        """ returns number of contacts displayed """
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def produce_contact_instance_from_maintable_row(self, contact_row):
        contact_cells = contact_row.find_elements_by_tag_name("td")

        contact_id = contact_cells[0].find_element_by_name("selected[]").get_attribute("value")
        fname = set_none_or_value_of(contact_cells[2].text)
        lname = set_none_or_value_of(contact_cells[1].text)
        primary_addr = set_none_or_value_of(contact_cells[3].text)
        all_emails = set_none_or_value_of(contact_cells[4].text)
        all_phones = set_none_or_value_of(contact_cells[5].text)

        return Contact(id=contact_id, fname=fname, lname=lname, primary_address=primary_addr,
                       phones_from_home_page=all_phones, emails_from_home_page=all_emails)

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()

            self.contacts_cache = []
            for contact_row in wd.find_elements_by_xpath("//tr[@name='entry']"):
                contact = self.produce_contact_instance_from_maintable_row(contact_row)

                self.contacts_cache.append(contact)

        return list(self.contacts_cache)

    def get_contact_info_from_home_page_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()

        contact_row = wd.find_elements_by_xpath("//tr[@name='entry']")[index]
        contact = self.produce_contact_instance_from_maintable_row(contact_row)

        return contact

    def get_contact_info_from_edit_page_by_index(self, index):
        self.open_contact_to_edit_by_index(index)

        cid = self.get_field_value("id")
        fname = self.get_field_value("firstname")
        lname = self.get_field_value("lastname")
        address = self.get_field_value("address")
        hphone = self.get_field_value("home")
        wphone = self.get_field_value("work")
        mobphone = self.get_field_value("mobile")
        secphone = self.get_field_value("phone2")
        email_1 = self.get_field_value("email")
        email_2 = self.get_field_value("email2")
        email_3 = self.get_field_value("email3")

        return Contact(id=cid, fname=fname, lname=lname, primary_address=address,
                       primary_phone=hphone, mobile_phone=mobphone, work_phone=wphone,
                       email_1=email_1, email_2=email_2, email_3=email_3,
                       secondary_phone=secphone)

    def get_contact_info_from_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        hphone = re.search("H: (.*)", text).group(1)
        mobphone = re.search("M: (.*)", text).group(1)
        wphone = re.search("W: (.*)", text).group(1)
        secphone = re.search("P: (.*)", text).group(1)

        return Contact(primary_phone=hphone, mobile_phone=mobphone,
                       work_phone=wphone, secondary_phone=secphone)
