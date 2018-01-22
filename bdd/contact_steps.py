
import random
from pytest_bdd import given, when, then

from model.contact import Contact

from utils.data_transformations import produce_instance_for_home_page_view


@given('a contact list')
def contact_list(db):
    return db.get_contacts_list()


@given('a contact with <fname>, <lname>, <primary_address>, <primary_phone>, <mobile_phone>, <work_phone>, <email_1>')
def new_contact(fname, lname, primary_address, primary_phone, mobile_phone, work_phone, email_1):
    return Contact(fname=fname, lname=lname, primary_address=primary_address,
                   primary_phone=primary_phone, mobile_phone=mobile_phone,
                   work_phone=work_phone, email_1=email_1)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(app, db, check_ui, new_contact, contact_list):
    old_contacts = contact_list

    if check_ui:
        assert len(old_contacts) + 1 == app.contacts.count()
    old_contacts.append(new_contact)

    new_contacts = db.get_contacts_list()
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)

    if check_ui:
        db_contacts_list = list(map(produce_instance_for_home_page_view, new_contacts))
        ui_contacts_list = app.contacts.get_contacts_list()
        assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contact(fname="contact for deletion"))

    return db.get_contacts_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete random contact from the list')
def delete_contact(app, random_contact):
    app.contacts.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(app, db, check_ui, random_contact, non_empty_contact_list):
    old_contacts = non_empty_contact_list

    if check_ui:
        assert len(old_contacts) - 1 == app.contacts.count()
    old_contacts.remove(random_contact)

    new_contacts = db.get_contacts_list()
    assert old_contacts == new_contacts

    if check_ui:
        db_contacts_list = list(map(produce_instance_for_home_page_view, new_contacts))
        ui_contacts_list = app.contacts.get_contacts_list()
        assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)


@given('a random contact to edit (from the list)')
def modification_data(non_empty_contact_list):
    return dict(contact_to_edit=random.choice(non_empty_contact_list))


@when('I modify random contact from the list')
def contact_after_modification(app, modification_data, contact_with_new_params):
    contact_with_new_params.id = modification_data['contact_to_edit'].id
    # Save contact we got after entering data on edit form.
    # This is necessary for cases when we don't change
    # some of fields.
    modification_data['ui_filled_contact_after_modification'] = app.contacts.edit_contact_by_id(contact_with_new_params)


@then('the new contact list is equal to the old contact list which got one contact modified')
def verify_contact_modified(app, db, check_ui, modification_data, non_empty_contact_list):
    old_contacts = non_empty_contact_list
    if check_ui:
        assert len(old_contacts) == app.contacts.count()
    old_contacts.remove(modification_data['contact_to_edit'])
    old_contacts.append(modification_data['ui_filled_contact_after_modification'])

    new_contacts = db.get_contacts_list()
    assert sorted(old_contacts, key=Contact.id_or_maxval) == sorted(new_contacts, key=Contact.id_or_maxval)

    if check_ui:
        db_contacts_list = list(map(produce_instance_for_home_page_view, new_contacts))
        ui_contacts_list = app.contacts.get_contacts_list()
        assert sorted(db_contacts_list, key=Contact.id_or_maxval) == sorted(ui_contacts_list, key=Contact.id_or_maxval)
