

class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        # checking specific checkbox presence - not only URL
        if not (wd.current_url.endswith("/index.php")
                and len(wd.find_elements_by_xpath("//form[@name='MainForm'][@id='MassCB']")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_group_page(self):
        wd = self.app.wd
        # checking specific button presence - not only URL
        if not (wd.current_url.endswith("/group.php")
                and len(wd.find_elements_by_xpath("//input[@name='new']")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
