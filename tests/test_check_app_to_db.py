def test_main_page(client):
    page = client.get('/')
    assert page.status_code == 200
    html = page.data.decode()
    assert '<!DOCTYPE html>' in html


def test_heights_pages(get_db_connection, client):
    ids = get_db_connection.select(['id'], 'heights')
    for i in ids:
        page = client.get(f'/edit_height/{i[0]}')
        assert page.status_code == 200
        html = page.data.decode()
        assert '<!DOCTYPE html>' in html
