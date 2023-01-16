from typing import Optional


class TreeStore:

    def __init__(self, input_items: list):
        self.items = input_items

    def get_all(self) -> list:
        return self.items

    def get_item(self, item_id: int) -> Optional[dict]:
        return next((item for item in self.items if item['id'] == item_id), None)

    def get_children(self, item_id: int) -> list:
        return [item for item in self.items if item.get('parent') == item_id]

    def get_all_parents(self, item_id: int) -> list:
        # начиная от самого элемента, чей id был передан в аргументе и до корневого элемента.
        # В задании есть такая строчка. То есть в parents должен быть и сам элемент, id которого передали
        # Но в примерах отдаются только предки, не включая входящий элемент.

        parents = []
        founded_item = self.get_item(item_id)
        if not founded_item:
            return []
        while founded_item.get('parent') != 'root':
            founded_parent = self.get_item(founded_item.get('parent'))
            parents.append(founded_parent)
            founded_item = founded_parent
        return parents
