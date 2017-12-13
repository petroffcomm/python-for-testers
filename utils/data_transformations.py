
import re
from model.contact import Contact
from model.group import Group


def clear_phone_for_table_view(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    phones = [contact.primary_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]
    processed_phones_list = list(filter(lambda i: i != "",
                                        list(map(lambda p: clear_phone_for_table_view(p),
                                                 filter(lambda i: i is not None,
                                                        phones)
                                                 )
                                             )
                                        )
                                 )
    if len(processed_phones_list) != 0:
        return '\n'.join(processed_phones_list)
    else:
        return None


def merge_emails_like_on_home_page(contact):
    emails = [contact.email_1, contact.email_2, contact.email_3]
    processed_emails_list = list(filter(lambda i: i is not None, emails))
    if len(processed_emails_list) != 0:
        return '\n'.join(processed_emails_list)
    else:
        return None


def set_none_or_value_of(val):
    if val == "":
        return None
    else:
        return val


def produce_instance_for_home_page_view(contact):
    return Contact(id=contact.id,
                   fname=set_none_or_value_of(contact.fname.strip()),
                   lname=set_none_or_value_of(contact.lname.strip()),
                   primary_address=set_none_or_value_of(contact.primary_address.strip()),
                   primary_phone=set_none_or_value_of(contact.primary_phone.strip()),
                   mobile_phone=set_none_or_value_of(contact.mobile_phone.strip()),
                   work_phone=set_none_or_value_of(contact.work_phone.strip()),
                   email_1=set_none_or_value_of(contact.email_1.strip()),
                   email_2=set_none_or_value_of(contact.email_2.strip()),
                   email_3=set_none_or_value_of(contact.email_3.strip()),
                   secondary_phone=set_none_or_value_of(contact.secondary_phone.strip())
                   )


def produce_instance_for_groups_page_view(group):
    # 1. We need to use 'set_none_or_value_of()' because some
    # objects in list we need to compare to current one
    # could be created with 'None'-value (but not empty string)
    # in the 'name'-field
    #
    # 2. We need to substitute multiple 'space'-chars to 1
    # because this is what application does for groups' names
    # 3. Web-browser trims edge 'space'-chars so we need to
    # take this into account.
    return Group(name=set_none_or_value_of(re.sub('\s+', ' ', group.name).strip()),
                 header=group.header,
                 footer=group.footer,
                 id=group.id
                 )
