import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contacts_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_table_view == merge_phones_like_in_table_view(contact_from_edit_page)


def test_phones_on_contacts_view_page(app):
    contact_from_view_page = app.contacts.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    # don't need to clear some symbols from phones
    assert contact_from_edit_page.primary_phone == contact_from_view_page.primary_phone
    assert contact_from_edit_page.mobile_phone == contact_from_view_page.mobile_phone
    assert contact_from_edit_page.work_phone == contact_from_view_page.work_phone
    assert contact_from_edit_page.secondary_phone == contact_from_view_page.secondary_phone


def clear_phone_for_table_view(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_in_table_view(contact):
    phones = [contact.primary_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]
    return '\n'.join(filter(lambda i: i != "",
                            list(
                                 map(
                                    lambda p: clear_phone_for_table_view(p),
                                    filter(lambda i: i is not None, phones)
                                    )
                                )
                            )
                     )
