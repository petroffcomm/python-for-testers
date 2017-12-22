# -*- coding: utf-8 -*-

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view


def test_add_group(app, db, check_ui, json_groups):
    old_groups = db.get_group_list()
    group = json_groups
    app.groups.create(group)

    if check_ui:
        assert len(old_groups) + 1 == app.groups.count()

    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)

    if check_ui:
        db_groups_list = list(map(produce_instance_for_groups_page_view, new_groups))
        ui_groups_list = app.groups.get_group_list()
        assert sorted(db_groups_list, key=Group.id_or_maxval) == sorted(ui_groups_list, key=Group.id_or_maxval)
