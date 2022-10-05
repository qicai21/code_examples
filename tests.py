from flask import template_rendered
from app import create_app
import pytest

@pytest.fixture()
def app():
    app = create_app()
    yield app

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

def test_return_403_while_post_without_csrf(app):
    response = app.test_client().post('/')
    assert response.status_code == 403
