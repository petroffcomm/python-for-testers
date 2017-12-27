from sys import maxsize


class Contact:
    def __init__(self, fname=None, mname=None, lname=None, primary_phone=None,
                 mobile_phone=None, work_phone=None, fax=None,
                 secondary_phone=None, email_1=None, email_2=None, email_3=None,
                 title=None, company=None, nickname=None, primary_address=None,
                 secondary_address=None, homepage=None, birthday_day=None,
                 birthday_month="-", birthday_year=None, anniversary_day=None,
                 anniversary_month="-", anniversary_year=None, notes=None, id=None,
                 phones_from_home_page=None, emails_from_home_page=None):
        self.id = id
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.primary_address = primary_address
        self.primary_phone = primary_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
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
        self.secondary_phone = secondary_phone
        self.phones_from_home_page = phones_from_home_page
        self.emails_from_home_page = emails_from_home_page
        self.notes = notes

    def __eq__(self, other):
        # in case when we come across empty "id"
        # we shouldn't take it into account
        ids_equal = (self.id is None or other.id is None or self.id == other.id)
        fnames_equal = (self.fname == other.fname)
        lnames_equal = (self.lname == other.lname)
        addr_equal = (self.primary_address == other.primary_address)
        hpage_emails_equal = (self.emails_from_home_page == other.emails_from_home_page)
        hpage_phones_equal = (self.phones_from_home_page == other.phones_from_home_page)
        return ids_equal and fnames_equal and lnames_equal and addr_equal and hpage_emails_equal and hpage_phones_equal

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.fname, self.lname, self.primary_address,
                                      self.emails_from_home_page, self.phones_from_home_page)

    def id_or_maxval(self):
        """Method used to compare 2 instances by 'id'-parameter.
        In case when some instance have empty 'id', method
        returns 'maxsize' const."""
        if self.id:
            return int(self.id)
        else:
            return maxsize
