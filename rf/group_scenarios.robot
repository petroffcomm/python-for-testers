*** Settings ***
Documentation    Test for AddressBook groups management
Library  Collections
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete group
    ${old_list}=  Get Group List
    ${group}=  Choose Group From List  ${old_list}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}
