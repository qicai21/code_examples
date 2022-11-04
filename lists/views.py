from flask import Blueprint, request, render_template, redirect
from lists.models import Item

lists_bp = Blueprint('lists', __name__)

@lists_bp.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        Item(text=request.form.get('item_text')).save()
        return redirect('/')
    items = Item.objects.all()
    return render_template('home.html', items=items)
