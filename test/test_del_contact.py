# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if not app.contact.is_any_contact_exists():
        app.contact.create(Contact(fname="contact for deletion"))

    app.contact.delete_first_contact()
