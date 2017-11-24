# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(fname="test fname", mname="test mname",
                               lname="test lname", nickname="test nickname",
                               title="test title", company="test company",
                               primary_address="test address", primary_address_phone="111",
                               mobile_phone="222", work_home="333", fax="444",
                               email_1="testemail1@test.test", email_2="testemail2@test.test",
                               email_3="testemail3@test.test", homepage="homepage.home",
                               birthday_day="5", birthday_month="January",
                               birthday_year="1969", anniversary_day="5",
                               anniversary_month="February", anniversary_year="2009",
                               secondary_address="test address2", secondary_address_phone="555",
                               notes="note note note note note note note note note note"
                                     "note note note note note note note note note note note note"))


def test_add_empty_contact(app):
    app.contact.create(Contact())
