def test_session(session):
    s = session
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    s.get('https://httpbin.org/cookies')
