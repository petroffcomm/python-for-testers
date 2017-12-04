# -*- coding: utf-8 -*-
from datetime import datetime
from random import randrange

from model.group import Group


date_str = datetime.now().__str__()
group_with_new_params = Group("new_name - " + date_str,
                              "new_header - " + date_str,
                              "new-footer - " + date_str)


#def test_edit_first_group(app):
#    if not app.groups.is_any_group_exists():
#        app.groups.create(Group(name="test group for full modification"))

#    old_groups = app.groups.get_group_list()
#    app.groups.edit_first_group(group_with_new_params)
#    new_groups = app.groups.get_group_list()
#    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if not app.groups.is_any_group_exists():
        app.groups.create(Group(name="test group for header modification"))

    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))

    group = Group(header="new header - " + date_str)
    # save 'id' for group to be modified (1-st group)
    group.id = old_groups[index].id
    # save 'name' for group to be modified (1-st group)
    group.name = old_groups[index].name
    app.groups.edit_group_by_index(index, group)

    assert len(old_groups) == app.groups.count()

    new_groups = app.groups.get_group_list()
    # replace 1-st group in old list (before modification)
    # by 'Group' instance which where used for modification
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)


def test_edit_first_group_name(app):
    if not app.groups.is_any_group_exists():
        app.groups.create(Group(name="test group for name modification"))

    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))

    group = Group(name="new name - " + date_str)
    group.id = old_groups[index].id

    app.groups.edit_group_by_index(index, group)

    assert len(old_groups) == app.groups.count()

    new_groups = app.groups.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)
