*** Settings ***
Documentation    Test for AddressBook contacts management
Library  Collections
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contacts List
    ${contact}=  New Contact
    Create Contact  ${contact}
    ${new_list}=  Get Contacts List
    Append To List  ${old_list}  ${contact}
    Contacts Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contacts List
    ${contact}=  Choose Contact From List  ${old_list}
    Delete Contact  ${contact}
    ${new_list}=  Get Contacts List
    Remove Values From List  ${old_list}  ${contact}
    Contacts Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contacts List
    ${contact_to_modify}=  Choose Contact From List  ${old_list}
    ${new_contact_data}=  New Contact
    ${contact_ui_data_after_modification}=  Modify Contact  ${contact_to_modify}  ${new_contact_data}
    ${new_list}=  Get Contacts List
    Remove Values From List  ${old_list}  ${contact_to_modify}
    Append To List  ${old_list}  ${contact_ui_data_after_modification}
    Contacts Lists Should Be Equal  ${new_list}  ${old_list}
