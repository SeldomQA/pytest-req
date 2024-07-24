def test_req_base_url(get):
    """
    test base url
    pytest --base-url=https://httpbin.org
    """
    payload = {'key1': 'value1', 'key2': 'value2'}
    s = get("/get", params=payload)
    assert s.status_code == 200


def test_session_base_url(session):
    """
    test session
    --base-url=https://httpbin.org
    """
    s = session
    s.get('/cookies/set/sessioncookie/123456789')
    s.get('/cookies')
