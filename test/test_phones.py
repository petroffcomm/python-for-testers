
from utils.data_transformations import *


def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contacts_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page_by_index(0)
    assert contact_from_home_page.phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# def test_phones_on_contacts_view_page(app):
#     contact_from_view_page = app.contacts.get_contact_info_from_view_page_by_index(0)
#     contact_from_edit_page = app.contacts.get_contact_info_from_edit_page_by_index(0)
#     # don't need to clear some symbols from phones
#     assert contact_from_edit_page.primary_phone.strip() == contact_from_view_page.primary_phone
#     assert contact_from_edit_page.mobile_phone.strip() == contact_from_view_page.mobile_phone
#     assert contact_from_edit_page.work_phone.strip() == contact_from_view_page.work_phone
#     assert contact_from_edit_page.secondary_phone.strip() == contact_from_view_page.secondary_phone
