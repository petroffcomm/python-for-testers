# -*- coding: utf-8 -*-
import random

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groups.create(Group(name="test group for deletion"))

    old_groups = db.get_group_list()
    group_to_delete = random.choice(old_groups)
    app.groups.delete_group_by_id(group_to_delete.id)

    if check_ui:
        assert len(old_groups) - 1 == app.groups.count()

    new_groups = db.get_group_list()
    old_groups.remove(group_to_delete)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)

    if check_ui:
        db_groups_list = list(map(produce_instance_for_groups_page_view, new_groups))
        ui_groups_list = app.groups.get_group_list()
        assert sorted(db_groups_list, key=Group.id_or_maxval) == sorted(ui_groups_list, key=Group.id_or_maxval)
