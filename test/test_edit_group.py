# -*- coding: utf-8 -*-
import pytest
from random import randrange

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view
from datagen.group import testdata


@pytest.mark.parametrize("new_group_data", testdata, ids=[repr(x) for x in testdata])
def test_edit_group(app, new_group_data):
    if not app.groups.is_any_group_exists():
        tmp_str = "test group modification"
        app.groups.create(Group(name=tmp_str, header=tmp_str, footer=tmp_str))

    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))
    # Save group we got after entering data on edit form.
    # This is necessary for cases when we don't change
    # some of fields.
    ui_filled_group_after_modification = app.groups.edit_group_by_index(index, new_group_data)

    assert len(old_groups) == app.groups.count()

    new_groups = app.groups.get_group_list()
    # transform source object to make him comparable
    # with what we see on groups page
    old_groups[index] = produce_instance_for_groups_page_view(ui_filled_group_after_modification)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)
