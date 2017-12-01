from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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
        wd = self.app.wd
        self.app.navigation.open_group_page()

        self.select_first_group()
        # init group editing
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_params)
        # submit modification saving
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()

        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.select_first_group()
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
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))

        return list(self.group_cache)
