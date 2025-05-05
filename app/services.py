from .repository import items_repo


# get all items or a specific item by id
def get_items(item_id=None):
    if item_id:
        return items_repo.get_by_id(item_id)
    return items_repo.get_all()


# add a new item to the repository
def add_item(name):
    items_repo.add({'name': name})


# update an existing item in the repository
def update_item(idx, name):
    success = items_repo.update(idx, {'name': name})
    return success
