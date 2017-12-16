# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            #self.wd = webdriver.Firefox(capabilities={"marionette": False},
            #                            firefox_binary=
            #                            "/media/WORK/JOB/education/software_testing/PythonForTesters/env/firefox_esr/firefox")
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                                        firefox_binary="/Applications/Firefox 2.app/Contents/MacOS/firefox")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)

        self.base_url = base_url

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
