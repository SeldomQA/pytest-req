from pytest_req.assertions import expect


def test_get_200(get):
    """
    test get request 200
    """
    s = get("https://httpbin.org/get")
    expect(s).to_be_ok()


def test_get_404(get):
    """
    test get request 404
    """
    s = get("https://httpbin.org/aaa")
    expect(s).to_have_status_code(404)


def test_get_assert_json(get):
    """
    test get request json
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
