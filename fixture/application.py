# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="/media/WORK/JOB/education/software_testing/PythonForTesters/env/firefox_esr/firefox")
        #self.wd = WebDriver(capabilities={"marionette": False},
        #                    firefox_binary="/Applications/Firefox 2.app/Contents/MacOS/firefox")
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.groups = GroupHelper(self)
        self.contacts = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
