import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        # flush cache after each request
        self.connection.autocommit(True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contacts_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, "
                           "home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, "
                           "aday, amonth, ayear, address2, phone2, notes "
                           "from addressbook where deprecated = %s", ('000-00-00 00:00:00'))
            for row in cursor:
                contact_list.append(Contact(id=str(row[0]), fname=row[1], mname=row[2], lname=row[3],
                                            nickname=row[4], company=row[5], title=row[6],
                                            primary_address=row[7], primary_phone=row[8], mobile_phone=row[9],
                                            work_phone=row[10], fax=row[11], email_1=row[12], email_2=row[13],
                                            email_3=row[14], homepage=row[15], birthday_day=row[16],
                                            birthday_month=row[17], birthday_year=row[18], anniversary_day=row[19],
                                            anniversary_month=row[20], anniversary_year=row[21], secondary_address=row[22],
                                            secondary_phone=row[23], notes=row[24]))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
