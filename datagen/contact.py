
import os.path
import jsonpickle
import getopt
import sys

from datagen.utils import *
from model.contact import Contact

# default values
contacts_qty = 5
target_file = "data/contacts.json"

# this part of code is not executed while importing this module -
# only while running itself
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file to write to"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    for option, arg in opts:
        if option == "-n":
            contacts_qty = int(arg)
        elif option == "-f":
            target_file = arg


testdata_for_adding = [Contact()] + [
            Contact(fname=rnd_name_string("fname", 15), mname=rnd_name_string("mname", 15),
                    lname=rnd_name_string("lname", 15), nickname="test nickname",
                    title="test title", company="test company", primary_address=random_string("address", 30),
                    primary_phone=rnd_phone_string(7), mobile_phone=rnd_phone_string(11),
                    work_phone=rnd_phone_string(7), fax=rnd_phone_string(7),
                    email_1=rnd_email(10, 7, ".ru"), email_2=rnd_email(10, 7, ".com"), email_3=rnd_email(10, 7, ".us"),
                    homepage="homepage.home", birthday_day="5", birthday_month="January", birthday_year="1969",
                    anniversary_day="5", anniversary_month="February", anniversary_year="2009",
                    secondary_address="test address2", secondary_phone=rnd_phone_string(11),
                    notes=random_string("some long note", 50))
            for i in range(contacts_qty)]

single_contact_with_rnd_data = Contact(fname=rnd_name_string("new fname", 15), lname=rnd_name_string("new lname", 15),
                                       primary_address=random_string("address", 30), primary_phone=rnd_phone_string(7),
                                       mobile_phone=rnd_phone_string(11), work_phone=rnd_phone_string(7),
                                       fax=rnd_phone_string(7), secondary_phone=rnd_phone_string(11),
                                       email_1=rnd_email(10, 7, ".ru"), email_2=rnd_email(10, 7, ".com"),
                                       email_3=rnd_email(10, 7, ".us"))

testdata_for_modifying = [Contact(fname=rnd_name_string("new fname", 15), lname=rnd_name_string("new lname", 15),
                                  primary_address=random_string("address", 30), primary_phone=rnd_phone_string(7),
                                  mobile_phone=rnd_phone_string(11), work_phone=rnd_phone_string(7),
                                  fax=rnd_phone_string(7), secondary_phone=rnd_phone_string(11),
                                  email_1=rnd_email(10, 7, ".ru"), email_2=rnd_email(10, 7, ".com"),
                                  email_3=rnd_email(10, 7, ".us"))
                          for i in range(contacts_qty)]

testdata = testdata_for_modifying

storage = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", target_file)

with open(storage, "w") as file:
    jsonpickle.set_decoder_options("json", indent=2)
    file.write(jsonpickle.encode(testdata))
