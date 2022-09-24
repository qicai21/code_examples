from app import app, home_page

def resolve(application, url):
    map = application.url_map.bind('', '/')
    endpoint = map.match(url)[0]
    return application.view_functions[endpoint]

def test_root_url_resolves_to_home_page_view():
    found = resolve(app, '/')
    assert found == home_page