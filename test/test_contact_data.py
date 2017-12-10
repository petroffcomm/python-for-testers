
from random import randrange
from datetime import datetime
from model.contact import Contact
from utils.data_transformations import *


def test_comparison_of_table_and_edit_views(app):
    if not app.contacts.is_any_contact_exists():
        date_str = datetime.now().timestamp().__str__()
        app.contacts.create(Contact(fname="new fname - " + date_str, lname="new lname - " + date_str,
                                    primary_address="new addr - " + date_str, primary_phone="1313",
                                    mobile_phone="2424", work_phone="3535", fax="4646",
                                    secondary_phone="5757", email_1="modified1@test.test",
                                    email_2="modified2@test.test", email_3="modified3@test.test"))

    index = randrange(app.contacts.count())
    contact_from_edit_page = produce_instance_for_home_page_view(
                                    app.contacts.get_contact_info_from_edit_page_by_index(index))
    contact_from_home_page = app.contacts.get_contact_info_from_home_page_by_index(index)
    assert contact_from_edit_page.fname == contact_from_home_page.fname
    assert contact_from_edit_page.lname == contact_from_home_page.lname
    assert contact_from_edit_page.primary_address == contact_from_home_page.primary_address

    assert merge_phones_like_on_home_page(contact_from_edit_page) == contact_from_home_page.phones_from_home_page
    assert merge_emails_like_on_home_page(contact_from_edit_page) == contact_from_home_page.emails_from_home_page
