from flask import Blueprint, request, render_template

lists_bp = Blueprint('lists', __name__)

@lists_bp.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html', new_item_text=request.form.get('item_text'))