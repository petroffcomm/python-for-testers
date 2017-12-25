import random

from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(app, orm):
    if len(orm.get_groups_with_contacts()) == 0:
        if len(orm.get_group_list()) == 0:
            tmp_str = "test group for placing contacts in here"
            app.groups.create(Group(name=tmp_str, header=tmp_str, footer=tmp_str))

        if len(orm.get_contacts_list()) == 0:
            app.contacts.create(Contact(fname="contact to be placed into group"))

        groups_list = orm.get_group_list()
        group_to_be_extended = random.choice(groups_list)
        contacts_list = orm.get_contacts_list()
        contact_to_be_placed_into_group = random.choice(contacts_list)

        app.contacts.add_contact_to_group(contact_to_be_placed_into_group, group_to_be_extended)

    groups_list = orm.get_groups_with_contacts()
    group_to_be_reduced = random.choice(groups_list)

    contacts_list = orm.get_contacts_in_group(group_to_be_reduced)
    contact_to_be_removed_from_group = random.choice(contacts_list)

    old_group_capacity = len(contacts_list)

    app.contacts.remove_contact_from_group(contact_to_be_removed_from_group, group_to_be_reduced)

    contacts_in_group_after_reducing = orm.get_contacts_in_group(group_to_be_reduced)
    new_group_capacity = len(contacts_in_group_after_reducing)

    assert new_group_capacity == old_group_capacity - 1
    assert contact_to_be_removed_from_group not in contacts_in_group_after_reducing
