import json
import os.path
import random

from fixture.application import Application
from fixture.db import DbFixture

from model.group import Group
from model.contact import Contact


from datagen.contact import single_contact_with_rnd_data as contact_with_rnd_data


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

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

        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.dbfixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    # Group methods
    def get_group_list(self):
        return self.dbfixture.get_group_list()

    # TODO: try to implement single method which can be used
    # to choose both groups and contacts
    def choose_group_from_list(self, groups):
        return random.choice(groups)

    def create_group(self, group):
        self.fixture.groups.create(group)

    def delete_group(self, group):
        self.fixture.groups.delete_group_by_id(group.id)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_maxval) == sorted(list2, key=Group.id_or_maxval)

    # Contact methods
    def get_contacts_list(self):
        return self.dbfixture.get_contacts_list()

    # TODO: try to implement single method which can be used
    # to choose both groups and contacts
    def choose_contact_from_list(self, contacts):
        return random.choice(contacts)

    def new_contact(self):
        return contact_with_rnd_data

    def create_contact(self, contact):
        self.fixture.contacts.create(contact)

    def delete_contact(self, contact):
        self.fixture.contacts.delete_contact_by_id(contact.id)

    def modify_contact(self, contact_to_modify, new_contact_data):
        new_contact_data.id = contact_to_modify.id
        # Save contact we got after entering data on edit form.
        # This is necessary for cases when we don't change
        # some of fields.
        return self.fixture.contacts.edit_contact_by_id(new_contact_data)

    def contacts_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_maxval) == sorted(list2, key=Contact.id_or_maxval)
