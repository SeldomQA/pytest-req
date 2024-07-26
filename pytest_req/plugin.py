import json

import pytest
import requests

from pytest_req.log import log

IMG = ["jpg", "jpeg", "gif", "bmp", "webp"]


class ResponseResult:
    status_code = 200
    response = None
    request = None


def formatting(msg):
    """formatted message"""
    if isinstance(msg, dict):
        return json.dumps(msg, indent=2, ensure_ascii=False)
    return msg


def request(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        log.info('-------------- Request -----------------[🚀]')
        if len(list(args)) == 1:
            url = list(args)[0]
        elif len(list(args)) == 2:
            url = list(args)[1]
        else:
            url = ""

        img_file = False
        file_type = url.split(".")[-1]
        if file_type in IMG:
            img_file = True

        req_method = func_name.replace("_", "")
        log.info(f"[method]: {req_method.upper()}      [url]: {url} ")
        auth = kwargs.get("auth", None)
        headers = kwargs.get("headers", None)
        cookies = kwargs.get("cookies", None)
        params = kwargs.get("params", None)
        data = kwargs.get("data", None)
        json_ = kwargs.get("json", None)
        files = kwargs.get("files", None)
        if auth is not None:
            log.debug(f"[auth]:\n{auth}")
        if headers is not None:
            log.debug(f"[headers]:\n{formatting(headers)}")
        if cookies is not None:
            log.debug(f"[cookies]:\n{formatting(cookies)}")
        if params is not None:
            log.debug(f"[params]:\n{formatting(params)}")
        if data is not None:
            log.debug(f"[data]:\n{formatting(data)}")
        if json_ is not None:
            log.debug(f"[json]:\n{formatting(json_)}")
        if files is not None:
            log.debug(f"[files]:\n{files}")

        # running function
        r = func(*args, **kwargs)

        ResponseResult.request = r.request
        ResponseResult.status_code = r.status_code
        log.info("-------------- Response ----------------[🛬️]")
        if ResponseResult.status_code == 200 or ResponseResult.status_code == 304:
            log.info(f"successful with status {ResponseResult.status_code}")
        else:
            log.warning(f"unsuccessful with status {ResponseResult.status_code}")
        resp_time = r.elapsed.total_seconds()
        try:
            resp = r.json()
            log.debug(f"[type]: json      [time]: {resp_time}")
            log.debug(f"[response]:\n {formatting(resp)}")
            ResponseResult.response = resp
        except BaseException as msg:
            log.debug("[warning]: failed to convert res to json, try to convert to text")
            log.trace(f"[warning]: {msg}")
            if img_file is True:
                log.debug(f"[type]: {file_type}      [time]: {resp_time}")
                ResponseResult.response = r.content
            else:
                r.encoding = 'utf-8'
                log.debug(f"[type]: text      [time]: {resp_time}")
                log.debug(f"[response]:\n {r.text}")
                ResponseResult.response = r.text

        return r

    return wrapper


class Session(requests.Session):

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    @request
    def get(self, url, **kwargs):
        r"""Sends a GET request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    @request
    def post(self, url, data=None, json=None, **kwargs):
        r"""Sends a POST request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        return self.request('POST', url, data=data, json=json, **kwargs)

    @request
    def put(self, url, data=None, **kwargs):
        r"""Sends a PUT request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        return self.request('PUT', url, data=data, **kwargs)

    @request
    def delete(self, url, **kwargs):
        r"""Sends a DELETE request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        return self.request('DELETE', url, **kwargs)

    @request
    def patch(self, url, data=None, **kwargs):
        r"""Sends a PATCH request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        return self.request("PATCH", url, data=data, **kwargs)

    @request
    def options(self, url, **kwargs):
        r"""Sends a OPTIONS request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        kwargs.setdefault("allow_redirects", True)
        return self.request("OPTIONS", url, **kwargs)

    @request
    def head(self, url, **kwargs):
        r"""Sends a HEAD request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        if (self.base_url is not None) and (url.startswith("http") is False):
            url = self.base_url + url
        kwargs.setdefault("allow_redirects", False)
        return self.request("HEAD", url, **kwargs)


@pytest.fixture
def get(base_url):
    @request
    def _get(url, params=None, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.get(url, params=params, **kwargs)

    return _get


@pytest.fixture
def post(base_url):
    @request
    def _post(url, data=None, json=None, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.post(url, data=data, json=json, **kwargs)

    return _post


@pytest.fixture
def put(base_url):
    @request
    def _put(url, data=None, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.put(url, data=data, **kwargs)

    return _put


@pytest.fixture
def delete(base_url):
    @request
    def _delete(url, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.delete(url, **kwargs)

    return _delete


@pytest.fixture
def patch(base_url):
    @request
    def _patch(url, data=None, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.patch(url, data=data, **kwargs)

    return _patch


@pytest.fixture
def head(base_url):
    @request
    def _head(url, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.head(url, **kwargs)

    return _head


@pytest.fixture
def options(base_url):
    @request
    def _options(url, **kwargs):
        if (base_url is not None) and (url.startswith("http") is False):
            url = base_url + url
        return requests.options(url, **kwargs)

    return _options


@pytest.fixture
def session(base_url):
    session = Session(base_url=base_url)

    yield session

    session.close()
