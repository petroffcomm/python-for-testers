from timeit import timeit
from model.group import Group
from utils.data_transformations import produce_instance_for_groups_page_view


def test_group_list(app, db):
    # ui_list = app.groups.get_group_list()
    print(timeit(lambda: app.groups.get_group_list(), number=1))
    # db_list = map(produce_instance_for_groups_page_view, db.get_group_list())
    print(timeit(lambda: map(produce_instance_for_groups_page_view, db.get_group_list()), number=1))
    # assert sorted(ui_list, key=Group.id_or_maxval) == sorted(db_list, key=Group.id_or_maxval)
    assert False
