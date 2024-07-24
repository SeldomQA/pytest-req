def test_get_method(get):
    """
    test get request
    --base-url=https://httpbin.org
    """
    payload = {'key1': 'value1', 'key2': 'value2'}
    s = get("/get", params=payload)
    assert s.status_code == 200


def test_session(session):
    """
    test session
    --base-url=https://httpbin.org
    """
    s = session
    s.get('/cookies/set/sessioncookie/123456789')
    s.get('/cookies')
