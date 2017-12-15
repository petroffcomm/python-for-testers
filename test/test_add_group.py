# -*- coding: utf-8 -*-

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view


def test_add_group(app, json_groups):
    old_groups = app.groups.get_group_list()

    group = json_groups
    app.groups.create(group)

    assert len(old_groups) + 1 == app.groups.count()

    new_groups = app.groups.get_group_list()
    # transform source object to make him comparable
    # with what we see on groups page
    old_groups.append(produce_instance_for_groups_page_view(group))
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)
