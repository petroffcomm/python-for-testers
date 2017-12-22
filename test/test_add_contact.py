# -*- coding: utf-8 -*-
from model.contact import Contact
from utils.data_transformations import produce_instance_for_home_page_view


def test_add_contact(app, db, check_ui, json_contacts):
    old_contacts = db.get_contacts_list()

    contact = json_contacts
    app.contacts.create(contact)

    if check_ui:
        assert len(old_contacts) + 1 == app.contacts.count()

    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)

    if check_ui:
        db_contacts_list = list(map(produce_instance_for_home_page_view, new_contacts))
        ui_contacts_list = app.contacts.get_contacts_list()
        assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)
