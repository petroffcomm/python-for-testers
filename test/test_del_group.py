# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group


def test_delete_some_group(app):
    if not app.groups.is_any_group_exists():
        app.groups.create(Group(name="test group for deletion"))

    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))
    app.groups.delete_group_by_index(index)

    assert len(old_groups) - 1 == app.groups.count()

    new_groups = app.groups.get_group_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
