from flask import Blueprint, render_template, request, redirect, url_for, flash
from .services import get_items, add_item, update_item

main_route = Blueprint('main', __name__)


@main_route.route('/', methods=['GET'])
def index():
    items = get_items()
    return render_template('index.html', items=items)


@main_route.route('/item/<int:item_id>', methods=['GET'])
def item_detail(item_id):
    item = get_items(item_id)
    if not item:
        flash('Item not found', 'error')
        return redirect(url_for('main.index'))
    return render_template('item.html', item=item)


@main_route.route('/save', methods=['POST'])
def save():
    # בדיקה האם זה עדכון או הוספה
    try:
        item_id = request.form.get('id', type=int)
    except ValueError:
        item_id = None
    name = request.form.get('name')
    if not name:
        flash('Name is required', 'error')
        return redirect(request.referrer)

    # אם קיים id -> עדכון
    if item_id:
        success = update_item(item_id, name)
        if not success:
            flash(f'Failed to update item with id {item_id}', 'error')
    else:
        add_item(name)

    return redirect(url_for('main.index'))