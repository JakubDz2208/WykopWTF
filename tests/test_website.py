import json
from flask.testing import FlaskClient
from pytest import mark


@mark.website
def test_index(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200

    assert b'<!DOCTYPE html>' in response.data
    assert b'<title>WykopWTF</title>' in response.data


@mark.website
def test_api_scrape_comments(client: FlaskClient):
    url = "example.com"
    limit = 5

    data = {'url': url, 'limit': limit}
    response = client.post('/api/scrape_comments', json=data)

    assert response.status_code == 200

    json_data = json.loads(response.data.decode('utf-8'))

    if 'comments' in json_data:
        assert len(json_data['comments']) == limit
    else:
        assert 'error' in json_data
        assert json_data['error'] == 'No comments available'