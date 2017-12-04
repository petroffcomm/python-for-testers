# -*- coding: utf-8 -*-
from datetime import datetime
from random import randrange

from model.contact import Contact

date_str = datetime.now().timestamp().__str__()
contact_with_new_params = Contact(fname="new fname - " + date_str, lname="new lname - " + date_str,
                                  primary_address="new addr - " + date_str, primary_address_phone="1313",
                                  mobile_phone="2424", work_home="3535", fax="4646",
                                  secondary_address_phone="5757", email_1="modified1@test.test",
                                  email_2="modified2@test.test", email_3="modified3@test.test")


def test_edit_first_contact(app):
    if not app.contacts.is_any_contact_exists():
        app.contacts.create(Contact(fname="contact for modification"))

    old_contacts = app.contacts.get_contacts_list()
    # save 'id' for contact to be modified (1-st group)
    index = randrange(len(old_contacts))
    contact_with_new_params.id = old_contacts[index].id
    app.contacts.edit_contact_by_index(index, contact_with_new_params)

    assert len(old_contacts) == app.contacts.count()

    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index] = contact_with_new_params
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)
