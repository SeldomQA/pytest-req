from pytest_req.assertions import expect


def test_status_code_ok(get):
    """
    assert http status code == 200
    """
    s = get("https://httpbin.org/get")
    expect(s).to_be_ok()


def test_assert_status_code_404(get):
    """
    assert HTTP status code == 404
    """
    s = get("https://httpbin.org/aaa")
    expect(s).to_have_status_code(404)


def test_assert_json_data(get):
    """
    assert json data
    """
    s = get("https://httpbin.org/get")
    json_str = {
        "args": {},
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
        },
        "url": "https://httpbin.org/get"
    }
    expect(s).to_have_json_matching(json_str, exclude=["X-Amzn-Trace-Id", "origin"])


def test_assert_path_value(get):
    """
    assert path value
    """
    s = get("https://httpbin.org/get")
    expect(s).to_have_path_value("headers.Host", "httpbin.org")


def test_assert_path_contains(get):
    """
    assert path value
    """
    s = get("https://httpbin.org/get")
    expect(s).to_have_path_contains("headers.Host", "httpbin.")


def test_assert_path_all_equal_success():
    """
    assert all values in list equal - success case
    """
    from pytest_req.assertions import Expect
    
    # Test with numeric values
    data1 = {
        "items": [1, 1, 1, 1, 1],
    }
    expect(data1).to_have_path_all_equal("items", 1)
    
    # Test with string values
    data2 = {
        "statuses": ["active", "active", "active"]
    }
    expect(data2).to_have_path_all_equal("statuses", "active")
