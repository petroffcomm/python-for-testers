# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.groups.get_group_list()

    group = Group(name="group1", header="group1", footer="group1")
    app.groups.create(group)

    new_groups = app.groups.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)


def test_add_empty_group(app):
    old_groups = app.groups.get_group_list()

    group = Group(name="", header="", footer="")
    app.groups.create(group)

    new_groups = app.groups.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)
