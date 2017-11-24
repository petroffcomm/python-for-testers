# -*- coding: utf-8 -*-
from datetime import datetime

from model.group import Group

date_str = datetime.now().__str__()
group_with_new_params = Group("new_name - " + date_str,
                              "new_header - " + date_str,
                              "new-footer - " + date_str)


def test_edit_first_group(app):
    if not app.group.is_any_group_exists():
        app.group.create(Group(name="test group for full modification"))

    app.group.edit_first_group(group_with_new_params)


def test_edit_first_group_header(app):
    if not app.group.is_any_group_exists():
        app.group.create(Group(name="test group for header modification"))

    app.group.edit_first_group(Group(header="new header - " + date_str))


def test_edit_first_group_name(app):
    if not app.group.is_any_group_exists():
        app.group.create(Group(name="test group for name modification"))

    app.group.edit_first_group(Group(name="new name - " + date_str))
