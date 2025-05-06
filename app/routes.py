from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .services import get_items, add_item, update_item, delete_item

main_route = Blueprint('main', __name__)


@main_route.before_request
def method_override():
    # Check if the request method is POST and if there is a form field named '_method'
    if request.method == 'POST' and '_method' in request.form:
        # Override the request method with the value of the '_method' field
        override_method = request.form['_method'].upper()
        print(f"Overriding method to: {override_method}")
        # if override_method in ['PUT', 'PATCH', 'DELETE'] and request.path.startswith('/items'):
        if override_method in ['PUT', 'PATCH', 'DELETE']:
            request.environ['REQUEST_METHOD'] = override_method


# GET - list of all items
@main_route.route('/', methods=['GET' , 'POST'])
def index():
    items = get_items()
    return render_template('index.html', items=items)


# GET - one item
@main_route.route('/item/<int:item_id>', methods=['GET'])
def item_detail(item_id):
    item = get_items(item_id)
    if not item:
        flash('Item not found', 'error')
        return redirect(url_for('main.index'))
    return render_template('item.html', item=item)


# @main_route.route('/items', methods=['POST', 'PUT', 'PATCH', 'DELETE'])
# def handle_items():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     new_method = data.get('_method')
#     if new_method:
#         request.environ['REQUEST_METHOD'] = new_method.upper()
#     method_override()
#     print(f"Received request: {request.method} {request.path}")
#     print(f"Request data: {request.data}")
#     if request.method == 'POST':
#         return create_item()
#     elif request.method in ['PUT', 'PATCH']:
#         return update_item_route()
#     elif request.method == 'DELETE':
#         return delete_item_route()


# # create new item
# def create_item():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     print(f"Received data to add new: {dict(data)}")
#     name = data.get('name')
#     if not name:
#         return jsonify({'error': 'Name is required'}), 400
#     add_item(name)
#     return redirect(url_for('main.index'))


# # update item
# def update_item_route():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     print(f"Received data to update: {dict(data)}")
#     name = data.get('name')
#     item_id = int(data.get('id'))
#     if not item_id:
#         return jsonify({'error': 'Item ID is required for update'}), 400
#     if not name:
#         return jsonify({'error': 'Name is required for update'}), 400
#     success = update_item(item_id, name)
#     if not success:
#         return jsonify({'error': 'Item not found'}), 404
#     # if request.is_json:
#     #     return jsonify({'id': item_id, 'name': name}), 200
#     return redirect(url_for('main.index'))


# # delete item
# def delete_item_route():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     print(f"Received data to delete: {dict(data)}")
#     item_id = int(data.get('id'))
#     success = delete_item(item_id)
#     if not success:
#         return jsonify({'error': 'Item not found'}), 404
#     # if request.is_json:
#     #     return jsonify({'message': f'Item {item_id} deleted'}), 200
#     return redirect(url_for('main.index'))


# POST - create new item
@main_route.route('/items', methods=['POST'])
def create_item():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    # print(f"Received data to add new: {dict(data)}")
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    add_item(name)
    return redirect(url_for('main.index'))


# PUT/PATCH - update item
@main_route.route('/items/update', methods=['POST', 'PUT', 'PATCH'])
def update_item_route():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    # print(f"Received data to update: {dict(data)}")
    name = data.get('name')
    item_id = int(data.get('id'))
    if not item_id:
        return jsonify({'error': 'Item ID is required for update'}), 400
    if not name:
        return jsonify({'error': 'Name is required for update'}), 400
    success = update_item(item_id, name)
    if not success:
        return jsonify({'error': 'Item not found'}), 404
    # if request.is_json:
    #     return jsonify({'id': item_id, 'name': name}), 200
    return redirect(url_for('main.index'))


# DELETE - delete item
@main_route.route('/items/delete', methods=['POST', 'DELETE'])
def delete_item_route():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    item_id = int(data.get('id'))
    success = delete_item(item_id)
    if not success:
        return jsonify({'error': 'Item not found'}), 404
    # if request.is_json:
    #     return jsonify({'message': f'Item {item_id} deleted'}), 200
    return redirect(url_for('main.index'))


# # POST - create new item
# @main_route.route('/items', methods=['POST'])
# def create_item():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     # print(f"Received data to add new: {dict(data)}")
#     name = data.get('name')
#     if not name:
#         return jsonify({'error': 'Name is required'}), 400
#     add_item(name)
#     return redirect(url_for('main.index'))


# # PUT/PATCH - update item
# @main_route.route('/items', methods=['PUT', 'PATCH'])
# def update_item_route():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     # print(f"Received data to update: {dict(data)}")
#     name = data.get('name')
#     item_id = int(data.get('id'))
#     if not item_id:
#         return jsonify({'error': 'Item ID is required for update'}), 400
#     if not name:
#         return jsonify({'error': 'Name is required for update'}), 400
#     success = update_item(item_id, name)
#     if not success:
#         return jsonify({'error': 'Item not found'}), 404
#     # if request.is_json:
#     #     return jsonify({'id': item_id, 'name': name}), 200
#     return redirect(url_for('main.index'))


# # DELETE - delete item
# @main_route.route('/items', methods=['DELETE'])
# def delete_item_route():
#     if request.is_json:
#         data = request.get_json()
#     else:
#         data = request.form
#     item_id = int(data.get('id'))
#     success = delete_item(item_id)
#     if not success:
#         return jsonify({'error': 'Item not found'}), 404
#     # if request.is_json:
#     #     return jsonify({'message': f'Item {item_id} deleted'}), 200
#     return redirect(url_for('main.index'))

