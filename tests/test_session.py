def test_session(session):
    """
    test session, keep requests cookie
    """
    s = session
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('https://httpbin.org/cookies')
    assert r.status_code == 200
    # ...
    r = s.patch('https://httpbin.org/patch')
    assert r.status_code == 200
    r = s.options('https://httpbin.org/get')
    assert r.status_code == 200
    r = s.options('https://httpbin.org/get')
    assert r.status_code == 200


def test_session_other(session):
    """
    test session
    Sessions can also be used to provide default data to the request methods
    """
    s = session
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})

    # both 'x-test' and 'x-test2' are sent
    s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
