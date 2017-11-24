# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if not app.group.is_any_group_exists():
        app.group.create(Group(name="test group for deletion"))

    app.group.delete_first_group()
