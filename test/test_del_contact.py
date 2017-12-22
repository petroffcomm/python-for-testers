# -*- coding: utf-8 -*-
import random

from model.contact import Contact
from utils.data_transformations import produce_instance_for_home_page_view


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contact(fname="contact for deletion"))

    old_contacts = db.get_contacts_list()
    contact_to_delete = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact_to_delete.id)

    if check_ui:
        assert len(old_contacts) - 1 == app.contacts.count()

    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact_to_delete)
    assert old_contacts == new_contacts

    if check_ui:
        db_contacts_list = list(map(produce_instance_for_home_page_view, new_contacts))
        ui_contacts_list = app.contacts.get_contacts_list()
        assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)
