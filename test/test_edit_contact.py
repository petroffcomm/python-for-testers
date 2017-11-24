# -*- coding: utf-8 -*-
from datetime import datetime

from model.contact import Contact

date_str = datetime.now().timestamp().__str__()
contact_with_new_params = Contact(fname="new fname - " + date_str, lname="new lname - " + date_str,
                                  primary_address="new addr - " + date_str, primary_address_phone="1313",
                                  mobile_phone="2424", work_home="3535", fax="4646",
                                  secondary_address_phone="5757", email_1="modified1@test.test",
                                  email_2="modified2@test.test", email_3="modified3@test.test")


def test_edit_first_contact(app):
    if not app.contact.is_any_contact_exists():
        app.contact.create(Contact(fname="contact for modification"))

    app.contact.edit_first_contact(contact_with_new_params)
