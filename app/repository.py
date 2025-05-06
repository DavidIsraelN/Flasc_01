class InMemoryRepo:
    def __init__(self):
        self._data = []
        self._id = 1


    def get_all(self):
        return self._data


    def get_by_id(self, idx):
        return next((x for x in self._data if x['id'] == idx), None)


    def add(self, item):
        item['id'] = self._id
        self._id += 1
        self._data.append(item)


    def update(self, idx, new_data):
        """
        update an item by id
        :param idx: id of the item to update
        """
        item = self.get_by_id(idx)
        if not item:
            return False
        # replace only the fields that are in new_data
        for key, value in new_data.items():
            if key != 'id':
                item[key] = value
        return True
    
    def delete(self, idx):
        item = self.get_by_id(idx)
        if not item:
            return False
        self._data.remove(item)
        return True


items_repo = InMemoryRepo()
