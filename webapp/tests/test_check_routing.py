def test_routes(client, get_routes):
    for route in get_routes:
        page = client.get(route)
        assert page.status_code
        html = page.data.decode()
        assert '<!DOCTYPE html>' in html
