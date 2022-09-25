from app import app, home_page

def resolve(application, url):
    map = application.url_map.bind('', '/')
    endpoint = map.match(url)[0]
    return application.view_functions[endpoint]

def test_root_url_resolves_to_home_page_view():
    found = resolve(app, '/')
    assert found == home_page

def test_home_page_returns_correct_html():
    response = home_page()
    html = response.data.decode('utf-8')
    print(html)
    assert html.startswith('<html>')
    assert '<title>To-Do lists</title>' in html
    assert html.endswith('</html>')