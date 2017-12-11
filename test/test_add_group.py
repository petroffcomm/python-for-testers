# -*- coding: utf-8 -*-
import pytest
import random
import string

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view


def random_string(prefix, maxlen):
    # '" "*10'-part is used to raise number of cases
    # when 'space'-char is returned
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.groups.get_group_list()

    app.groups.create(group)

    assert len(old_groups) + 1 == app.groups.count()

    new_groups = app.groups.get_group_list()
    # transform source object to make him comparable
    # with what we see on groups page
    old_groups.append(produce_instance_for_groups_page_view(group))
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)
