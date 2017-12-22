# -*- coding: utf-8 -*-
import pytest
import random

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view
from datagen.group import testdata


@pytest.mark.parametrize("new_group_data", testdata, ids=[repr(x) for x in testdata])
def test_edit_group(app, db, check_ui, new_group_data):
    if len(db.get_group_list()) == 0:
        tmp_str = "test group modification"
        app.groups.create(Group(name=tmp_str, header=tmp_str, footer=tmp_str))

    old_groups = db.get_group_list()
    group_to_edit = random.choice(old_groups)
    # Save group we got after entering data on edit form.
    # This is necessary for cases when we don't change
    # some of fields.
    ui_filled_group_after_modification = app.groups.edit_group_by_id(group_to_edit.id, new_group_data)

    if check_ui:
        assert len(old_groups) == app.groups.count()

    new_groups = db.get_group_list()
    # replace object with its new version
    old_groups.remove(group_to_edit)
    old_groups.append(ui_filled_group_after_modification)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)

    if check_ui:
        db_groups_list = list(map(produce_instance_for_groups_page_view, new_groups))
        ui_groups_list = app.groups.get_group_list()
        assert sorted(db_groups_list, key=Group.id_or_maxval) == sorted(ui_groups_list, key=Group.id_or_maxval)
