Scenario Outline: Add new contact
  Given a contact list
  And a contact with <fname>, <lname>, <primary_address>, <primary_phone>, <mobile_phone>, <work_phone>, <email_1>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact
  # this can be implemented without table - in a way like we used to test modification
  Examples:
  |     fname    |    lname     | primary_address | primary_phone | mobile_phone | work_phone |    email_1    |
  | test_fname_1 | test_fname_1 | test_address_1  | 223322        | +38034566    | 057666998  | test1@mail.ru |
  | test_fname_2 | test_fname_2 | test_address_3  | 332233        | +38034567    | 057666999  | test2@mail.ru |


  Scenario: Delete a contact
  Given a non-empty contact list
  And a random contact from the list
  When I delete random contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact


  Scenario: Modify a contact
  Given a non-empty contact list
  And a random contact to edit (from the list)
  When I modify random contact from the list
  Then the new contact list is equal to the old contact list which got one contact modified
