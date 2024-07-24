def test_session(session):
    """
    test session, keep requests cookie
    """
    s = session
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    s.get('https://httpbin.org/cookies')
