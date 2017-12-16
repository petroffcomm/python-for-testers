# -*- coding: utf-8 -*-
from random import randrange

import pytest

from model.contact import Contact
from utils.data_transformations import produce_instance_for_home_page_view
from datagen.contact import testdata_for_adding


@pytest.mark.parametrize("contact_with_new_params", testdata_for_adding, ids=[repr(x) for x in testdata_for_adding])
def test_edit_first_contact(app, contact_with_new_params):
    if not app.contacts.is_any_contact_exists():
        app.contacts.create(Contact(fname="contact for modification"))

    old_contacts = app.contacts.get_contacts_list()
    # save 'id' for contact to be modified (1-st group)
    index = randrange(len(old_contacts))
    contact_with_new_params.id = old_contacts[index].id
    # Save contact we got after entering data on edit form.
    # This is necessary for cases when we don't change
    # some of fields.
    ui_filled_contact_after_modification = app.contacts.edit_contact_by_index(index, contact_with_new_params)

    assert len(old_contacts) == app.contacts.count()

    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index] = produce_instance_for_home_page_view(ui_filled_contact_after_modification)
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)
