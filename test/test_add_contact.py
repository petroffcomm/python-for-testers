# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    old_contacts = app.contacts.get_contacts_list()

    contact = json_contacts
    app.contacts.create(contact)

    assert len(old_contacts) + 1 == app.contacts.count()

    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)
