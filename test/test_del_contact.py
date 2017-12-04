# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_delete_first_contact(app):
    if not app.contacts.is_any_contact_exists():
        app.contacts.create(Contact(fname="contact for deletion"))

    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)

    assert len(old_contacts) - 1 == app.contacts.count()

    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
