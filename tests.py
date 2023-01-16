from simple import TreeStore
from with_save_data import TreeStore as TreStoreSavedData


def test_get_all():
    assert ts.get_all() == items


def test_get_item():
    assert ts.get_item(7) == {"id": 7, "parent": 4, "type": None}
    assert ts.get_item(1) == {"id": 1, "parent": "root"}
    assert ts.get_item(4) == {"id": 4, "parent": 2, "type": "test"}


def test_get_children():
    assert ts.get_children(4) == [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]
    assert ts.get_children(5) == []


def test_get_all_parents():
    assert ts.get_all_parents(7) == [
        {"id": 4, "parent": 2, "type": "test"}, {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"}
    ]
    assert ts.get_all_parents(4) == [{"id": 2, "parent": 1, "type": "test"}, {"id": 1, "parent": "root"}]
    assert ts.get_all_parents(1) == []


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)
    test_get_all()
    test_get_item()
    test_get_children()
    test_get_all_parents()

    ts = TreStoreSavedData(items)
    test_get_all()
    test_get_item()
    test_get_children()
    test_get_all_parents()
