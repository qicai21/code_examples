from flask import template_rendered
from app import app

def test_uses_home_template():
    template_used = None
    def captrue_template_rendered(sender, template, **extra):
        nonlocal template_used
        template_used = template
    template_rendered.connect(captrue_template_rendered, app)
    app.test_client().get('/')
    assert template_used.name == 'home.html'