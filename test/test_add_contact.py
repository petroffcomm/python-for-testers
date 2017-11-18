# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
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
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(fname="", mname="", lname="", nickname="",
                               title="", company="", primary_address="",
                               primary_address_phone="", mobile_phone="",
                               work_home="", fax="", email_1="", email_2="",
                               email_3="", homepage="", birthday_day="",
                               birthday_month="-", birthday_year="",
                               anniversary_day="", anniversary_month="-",
                               anniversary_year="", secondary_address="",
                               secondary_address_phone="", notes=""))

    app.session.logout()
