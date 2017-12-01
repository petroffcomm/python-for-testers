# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if not app.groups.is_any_group_exists():
        app.groups.create(Group(name="test group for deletion"))

    old_groups = app.groups.get_group_list()
    app.groups.delete_first_group()
    new_groups = app.groups.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

    old_groups[0:1] = []
    assert old_groups == new_groups
