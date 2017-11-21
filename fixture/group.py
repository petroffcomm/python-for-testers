
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.app.navigation.open_group_page()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.navigation.return_to_groups_page()

    def edit_first_group(self, new_params):
        wd = self.app.wd
        self.app.navigation.open_group_page()

        # select group to edit
        wd.find_element_by_name("selected[]").click()
        # init group editing
        wd.find_element_by_name("edit").click()

        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(new_params.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(new_params.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(new_params.footer)

        # submit modification saving
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        # select group to delete
        wd.find_element_by_name("selected[]").click()
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()
