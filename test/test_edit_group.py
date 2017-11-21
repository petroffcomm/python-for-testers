# -*- coding: utf-8 -*-
from datetime import datetime

from model.group import Group

date_str = datetime.now().__str__()
group_with_new_params = Group("new_name - " + date_str,
                              "new_header - " + date_str,
                              "new-footer - " + date_str)


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group_with_new_params)
    app.session.logout()
