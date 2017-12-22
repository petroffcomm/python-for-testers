# -*- coding: utf-8 -*-
import random
import pytest

from model.contact import Contact
from utils.data_transformations import produce_instance_for_home_page_view
from datagen.contact import testdata_for_adding


@pytest.mark.parametrize("contact_with_new_params", testdata_for_adding, ids=[repr(x) for x in testdata_for_adding])
def test_edit_first_contact(app, db, check_ui, contact_with_new_params):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contact(fname="contact for modification"))

    old_contacts = db.get_contacts_list()
    # save 'id' for contact to be modified (1-st group)
    contact_to_edit = random.choice(old_contacts)
    contact_with_new_params.id = contact_to_edit.id
    # Save contact we got after entering data on edit form.
    # This is necessary for cases when we don't change
    # some of fields.
    ui_filled_contact_after_modification = app.contacts.edit_contact_by_id(contact_with_new_params)

    if check_ui:
        assert len(old_contacts) == app.contacts.count()

    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact_to_edit)
    old_contacts.append(ui_filled_contact_after_modification)
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)

    if check_ui:
        db_contacts_list = list(map(produce_instance_for_home_page_view, new_contacts))
        ui_contacts_list = app.contacts.get_contacts_list()
        assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)
