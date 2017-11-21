
class Contact:
    def __init__(self, fname, mname, lname, primary_address_phone, mobile_phone, work_home,
                       fax, secondary_address_phone, email_1, email_2, email_3,
                       title=None, company=None, nickname=None, primary_address=None,
                       secondary_address=None, homepage=None, birthday_day=None,
                       birthday_month="-", birthday_year=None, anniversary_day=None,
                       anniversary_month="-", anniversary_year=None, notes=None):

        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.primary_address = primary_address
        self.primary_address_phone = primary_address_phone
        self.mobile_phone = mobile_phone
        self.work_home = work_home
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.secondary_address = secondary_address
        self.secondary_address_phone = secondary_address_phone
        self.notes = notes
