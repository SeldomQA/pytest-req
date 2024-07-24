def test_put_method(put):
    """
    test put request
    """
    s = put('https://httpbin.org/put', data={'key': 'value'})
    assert s.status_code == 200


def test_post_method(post):
    """
    test post request
    """
    s = post('https://httpbin.org/post', data={'key': 'value'})
    assert s.status_code == 200


def test_get_method(get):
    """
    test get request
    """
    payload = {'key1': 'value1', 'key2': 'value2'}
    s = get("https://httpbin.org/get", params=payload)
    assert s.status_code == 200


def test_delete_method(delete):
    """
    test delete request
    """
    s = delete('https://httpbin.org/delete')
    assert s.status_code == 200
