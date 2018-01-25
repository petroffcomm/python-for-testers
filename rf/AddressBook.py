import json
import os.path

from fixture.application import Application
from fixture.db import DbFixture

from model.group import Group


class AddressBook:

    def __init__(self, config_file="target.json", browser="firefox"):
        self.browser = browser

        config = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config_file)
        with open(config_file) as config:
            self.target = json.load(config)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])

        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                                   user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.dbfixture.destroy()

    def create_group(self, name, header, footer):
        self.fixture.groups.create(Group(name=name, header=header, footer=footer))
