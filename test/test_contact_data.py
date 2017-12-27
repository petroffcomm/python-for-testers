
from datetime import datetime
from model.contact import Contact
from utils.data_transformations import produce_instance_for_home_page_view


def test_comparison_of_table_and_edit_views(app, orm):
    if not app.contacts.is_any_contact_exists():
        date_str = datetime.now().timestamp().__str__()
        app.contacts.create(Contact(fname="new fname - " + date_str, lname="new lname - " + date_str,
                                    primary_address="new addr - " + date_str, primary_phone="1313",
                                    mobile_phone="2424", work_phone="3535", fax="4646",
                                    secondary_phone="5757", email_1="modified1@test.test",
                                    email_2="modified2@test.test", email_3="modified3@test.test"))

    db_contacts_list = list(map(produce_instance_for_home_page_view, orm.get_contacts_list()))
    ui_contacts_list = app.contacts.get_contacts_list()
    assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)
