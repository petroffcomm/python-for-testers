from model.group import Group
from utils.data_transformations import set_none_or_value_of


class GroupHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def set_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_field_value(self, field_name):
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value")

    def fill_group_form(self, group):
        self.set_field_value("group_name", group.name)
        self.set_field_value("group_header", group.header)
        self.set_field_value("group_footer", group.footer)

    def get_form_data(self):
        return Group(id=self.get_field_value("id"),
                     name=self.get_field_value("group_name"),
                     header=self.get_field_value("group_header"),
                     footer=self.get_field_value("group_footer"))

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.app.navigation.open_group_page()
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.navigation.return_to_groups_page()

        self.group_cache = None

    def edit_first_group(self, new_params):
        self.edit_group_by_index(0, new_params)

    def edit_group_by_index(self, index, new_params):
        wd = self.app.wd
        self.app.navigation.open_group_page()

        self.select_group_by_index(index)
        # init group editing
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_params)

        # save modified group data to the 'group'-object
        modified_group_data = self.get_form_data()
        # submit modification saving
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()

        self.group_cache = None

        return modified_group_data

    def edit_group_by_id(self, id, new_params):
        wd = self.app.wd
        self.app.navigation.open_group_page()

        self.select_group_by_id(id)
        # init group editing
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_params)

        # save modified group data to the 'group'-object
        modified_group_data = self.get_form_data()
        # submit modification saving
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()

        self.group_cache = None

        return modified_group_data

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.select_group_by_index(index)
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()

        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.select_group_by_id(id)
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()

        self.group_cache = None

    def is_any_group_exists(self):
        """ returns True if at least 1 group is displayed """
        wd = self.app.wd
        self.app.navigation.open_group_page()
        return len(wd.find_elements_by_name("selected[]")) != 0

    def count(self):
        """ returns number of group items displayed """
        wd = self.app.wd
        self.app.navigation.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.open_group_page()
            self.group_cache = []

            for element in wd.find_elements_by_css_selector('span.group'):
                # we need to use 'set_none_or_value_of()' because some objects
                # in list we need to compare to current one
                # could be created with 'None'-value (but not empty string)
                # in the 'name'-field
                text = set_none_or_value_of(element.text)
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))

        return list(self.group_cache)
