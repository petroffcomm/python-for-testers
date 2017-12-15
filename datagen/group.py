
import os.path
import jsonpickle
import getopt
import sys

from datagen.utils import random_string
from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file to write to"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    sys.exit(2)

groups_qty = 5
target_file = "data/groups.json"

for option, arg in opts:
    if option == "-n":
        groups_qty = int(arg)
    elif option == "-f":
        target_file = arg

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(groups_qty)
]

storage = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", target_file)

with open(storage, "w") as file:
    jsonpickle.set_decoder_options("json", indent=2)
    file.write(jsonpickle.encode(testdata))
