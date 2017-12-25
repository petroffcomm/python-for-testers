
from fixture.orm import ORMFixture
from model.group import Group

connection = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    #l = connection.get_contacts_not_in_group(Group(id='268'))
    l = connection.get_groups_with_contacts()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #connection.destroy()
