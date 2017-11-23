# -*- coding: utf-8 -*-
from datetime import datetime

from model.group import Group

date_str = datetime.now().__str__()
group_with_new_params = Group("new_name - " + date_str,
                              "new_header - " + date_str,
                              "new-footer - " + date_str)


def test_edit_first_group(app):
    app.group.edit_first_group(group_with_new_params)


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="new header - " + date_str))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="new name - " + date_str))
