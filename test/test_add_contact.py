# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from utils.testdata_gen import *


testdata = [Contact(fname=rnd_name_string("fname", 15), mname=rnd_name_string("mname", 15),
                    lname=rnd_name_string("lname", 15), nickname="test nickname",
                    title="test title", company="test company", primary_address=random_string("address", 30),
                    primary_phone=rnd_phone_string(7), mobile_phone=rnd_phone_string(11),
                    work_phone=rnd_phone_string(7), fax=rnd_phone_string(7),
                    email_1=rnd_email(10, 7, ".ru"), email_2=rnd_email(10, 7, ".com"), email_3=rnd_email(10, 7, ".us"),
                    homepage="homepage.home", birthday_day="5", birthday_month="January", birthday_year="1969",
                    anniversary_day="5", anniversary_month="February", anniversary_year="2009",
                    secondary_address="test address2", secondary_phone=rnd_phone_string(11),
                    notes=random_string("some long note", 50))] +\
           [Contact()]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contacts_list()

    app.contacts.create(contact)

    assert len(old_contacts) + 1 == app.contacts.count()

    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)
