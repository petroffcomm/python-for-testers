*** Settings ***
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    Create Group  name1  header1  footer1
