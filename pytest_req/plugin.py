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
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")

        img_file = False
        file_type = url.split(".")[-1]
        if file_type in IMG:
            img_file = True

        log.info(f"[method]: {func_name.upper()}      [url]: {url} ")
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


@pytest.fixture
def get():
    @request
    def _get(url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)

    return _get


@pytest.fixture
def post():
    @request
    def _post(url, data=None, json=None, **kwargs):
        return requests.post(url, data=data, json=json, **kwargs)

    return _post


@pytest.fixture
def put():
    @request
    def _put(url, data=None, **kwargs):
        return requests.put(url, data=data, **kwargs)

    return _put


@pytest.fixture
def delete():
    @request
    def _delete(url, **kwargs):
        return requests.delete(url, **kwargs)

    return _delete


@pytest.fixture(scope="function")
def patch():
    @request
    def _patch(url, data=None, **kwargs):
        return requests.patch(url, data=data, **kwargs)

    return _patch
