
class GroupHelper:
    def __init__(self, app):
        self.app = app

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

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.select_first_group()
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()