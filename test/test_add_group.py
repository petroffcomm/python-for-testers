# -*- coding: utf-8 -*-
import pytest

from model.group import Group
from utils.testdata_gen import random_string
from utils.data_transformations import produce_instance_for_groups_page_view


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
