from datetime import datetime
from pony.orm import *
from pymysql.converters import encoders, decoders, convert_mysql_timestamp

from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        # 'lazy'-option extracts data from DB only when a reference to corresponding field occurs.
        # This prevents DB from serving too huge load when populating large data-structures
        # with a lot of table references/cross-references.
        contacts = Set(lambda: ORMFixture.ORMContact,
                       table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str, column='title')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        bday = Optional(int, column='bday')
        bmonth = Optional(str, column='bmonth')
        byear = Optional(str, column='byear')
        aday = Optional(int, column='aday')
        amonth = Optional(str, column='amonth')
        ayear = Optional(str, column='ayear')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        notes = Optional(str, column='notes')
        deprecated = Optional(str, column='deprecated')

        groups = Set(lambda: ORMFixture.ORMGroup,
                     table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    def destroy(self):
        self.db.disconnect()

    def convert_db_groups_to_model_groups(self, groups):
        def convert(db_obj):
            return Group(id=str(db_obj.id), name=db_obj.name, header=db_obj.header, footer=db_obj.footer)
        return list(map(convert, groups))

    def convert_db_contacts_to_model_contacts(self, groups):
        def convert(db_obj):
            return Contact(id=str(db_obj.id), fname=db_obj.firstname, lname=db_obj.lastname,
                           primary_address=db_obj.address, primary_phone=db_obj.home,
                           mobile_phone=db_obj.mobile, work_phone=db_obj.work, email_1=db_obj.email,
                           email_2=db_obj.email2, email_3=db_obj.email3, secondary_phone=db_obj.phone2)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_db_groups_to_model_groups(list(select(g for g in ORMFixture.ORMGroup)))

    @db_session
    def get_contacts_list(self):
        return self.convert_db_contacts_to_model_contacts(list(select(c for c in ORMFixture.ORMContact
                                                                      if c.deprecated is None)))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_db_contacts_to_model_contacts(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]

        return self.convert_db_contacts_to_model_contacts(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_groups_with_contacts(self):
        orm_groups = select(g for g in ORMFixture.ORMGroup if count(g.contacts) > 0)
        return self.convert_db_groups_to_model_groups(list(orm_groups))
    # def get_group_list(self):
    #     with db_session:
    #         return list(select(g for g in ORMFixture.ORMGroup))
