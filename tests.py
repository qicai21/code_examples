from flask import template_rendered
from app import create_app
from models import Item
from mongoengine import connect, disconnect
import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    disconnect()
    connect(
        db='mongoenginetest', 
        host='mongomock://localhost',
        uuidRepresentation="pythonLegacy")
    yield app
    disconnect()


@pytest.fixture()
def capture_template_while_render(app):
    template_used = []
    def capture_template(sender, template, **extra):
        template_used.append(template.name)
    template_rendered.connect(capture_template, app)
    try:
        yield template_used
    finally:
        template_rendered.disconnect(capture_template, app)


def test_use_home_template(app, capture_template_while_render):
    app.test_client().get('/')
    template_used = capture_template_while_render[0]
    assert template_used == 'home.html'


def test_return_403_while_post_without_csrf():
    app = create_app()
    response = app.test_client().post('/')
    assert response.status_code == 403

def test_can_save_a_post_request(app, capture_template_while_render):
    text =  'A new list item'
    client = app.test_client()
    response = client.post('/', data={'item_text': text}) 
    assert 'A new list item' in response.data.decode('utf-8')
    assert capture_template_while_render[0] == 'home.html'

def test_saving_and_retrieving_items(app):
    first_item = Item()
    first_item.text = 'The first (ever) list item'
    first_item.save()

    second_item = Item()
    second_item.text = 'Item the second'
    second_item.save()

    saved_items = Item.objects.all()
    assert saved_items.count() == 2
    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    assert first_saved_item.text == 'The first (ever) list item'
    assert second_saved_item.text == 'Item the second'