from typing import Optional


class TreeStore:

    def __init__(self, input_items: list):
        self.items = input_items
        self.children_data = {}
        self.parents_data = {}

        for item in self.items:
            self.children_data[item.get('id')] = self._get_children(item.get('id'))
            self.parents_data[item.get('id')] = self._get_all_parents(item.get('id'))

    def get_all(self) -> list:
        return self.items

    def get_item(self, item_id: int) -> Optional[dict]:
        return next((item for item in self.items if item['id'] == item_id), None)

    def _get_children(self, item_id: int) -> list:
        return [item for item in self.items if item.get('parent') == item_id]

    def _get_all_parents(self, item_id: int) -> list:
        # "начиная от самого элемента, чей id был передан в аргументе и до корневого элемента."
        # В задании есть такая строчка. То есть в parents должен быть и сам элемент, id которого передали
        # Но в примерах отдаются только предки, не включая входящий элемент.

        parents = []
        founded_item = self.get_item(item_id)
        if not founded_item:
            return []
        while founded_item.get('parent') != 'root':
            founded_item = self.get_item(founded_item.get('parent'))
            parents.append(founded_item)
        return parents

    def get_children(self, item_id: int) -> list:
        return self.children_data.get(item_id, [])

    def get_all_parents(self, item_id: int) -> list:
        return self.parents_data.get(item_id, [])

