import random
from pytest_bdd import given, when, then

from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header>, <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.groups.create(new_group)


@then('the new group list is equal to the old group list (with the added group)')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    old_groups.append(new_group)

    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.groups.create(Group(name="test group for deletion"))

    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.groups.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old group list (without the deleted group)')
def verify_group_deleted(app, db, check_ui, non_empty_group_list, random_group):
    old_groups = non_empty_group_list

    if check_ui:
        assert len(old_groups) - 1 == app.groups.count()

    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert sorted(old_groups, key=Group.id_or_maxval) == sorted(new_groups, key=Group.id_or_maxval)

    if check_ui:
        db_groups_list = list(map(produce_instance_for_groups_page_view, new_groups))
        ui_groups_list = app.groups.get_group_list()
        assert sorted(db_groups_list, key=Group.id_or_maxval) == sorted(ui_groups_list, key=Group.id_or_maxval)
