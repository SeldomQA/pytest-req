# pytest-req

> pytest requests plugin

pytest 使用 requests 库的插件。

## 安装

```shell
pip install pytest-req
```

## 使用

pytest-req 完全兼容 [Requests](https://docs.python-requests.org/en/master/) API 如下:

| pytest-req(fixture) | requests           |
|---------------------|--------------------|
| get()               | requests.get()     |
| post()              | requests.post()    |
| put()               | requests.put()     |
| delete()            | requests.delete()  |
| patch()             | requests.patch()   |
| session()           | requests.session() |

👉︎ [查看测试](./tests)

__⭐ 支持简单的请求__

```python

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
```

__⭐ 支持Session__

```python

def test_session(session):
    s = session
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    s.get('https://httpbin.org/cookies')
```

__⭐ 支持base-url__

```python

def test_get_method(get):
    """
    test get request
    --base-url=https://httpbin.org
    """
    payload = {'key1': 'value1', 'key2': 'value2'}
    s = get("/get", params=payload)
    assert s.status_code == 200
```

更多的使用方式参考 requests 文档。

__✅ 运行测试__

```shell
> pytest -s  # 运行当前所有用例
> pytest -s test_req.py # 运行指定文件
> pytest -s --base-url=https://httpbin.org  # 指定base-url
```

更多的运行方式请参考 pytest 文档。

__🗒 运行日志__

```shell
> pytest -qs --base-url=https://httpbin.org test_base_url.py
2024-07-24 12:18:39 | INFO     | plugin.py | -------------- Request -----------------[🚀]
2024-07-24 12:18:39 | INFO     | plugin.py | [method]: GET      [url]: /get 
2024-07-24 12:18:39 | DEBUG    | plugin.py | [params]:
{
  "key1": "value1",
  "key2": "value2"
}
2024-07-24 12:18:40 | INFO     | plugin.py | -------------- Response ----------------[🛬️]
2024-07-24 12:18:40 | INFO     | plugin.py | successful with status 200
2024-07-24 12:18:40 | DEBUG    | plugin.py | [type]: json      [time]: 1.655213
2024-07-24 12:18:40 | DEBUG    | plugin.py | [response]:
 {
  "args": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-66a080a0-2cb150485a260ae75b34b32f"
  },
  "origin": "171.10.176.209",
  "url": "https://httpbin.org/get?key1=value1&key2=value2"
}
.2024-07-24 12:18:40 | INFO     | plugin.py | -------------- Request -----------------[🚀]
2024-07-24 12:18:40 | INFO     | plugin.py | [method]: GET      [url]: /cookies/set/sessioncookie/123456789 
2024-07-24 12:18:43 | INFO     | plugin.py | -------------- Response ----------------[🛬️]
2024-07-24 12:18:43 | INFO     | plugin.py | successful with status 200
2024-07-24 12:18:43 | DEBUG    | plugin.py | [type]: json      [time]: 0.807398
2024-07-24 12:18:43 | DEBUG    | plugin.py | [response]:
 {
  "cookies": {
    "sessioncookie": "123456789"
  }
}
2024-07-24 12:18:43 | INFO     | plugin.py | -------------- Request -----------------[🚀]
2024-07-24 12:18:43 | INFO     | plugin.py | [method]: GET      [url]: /cookies 
2024-07-24 12:18:44 | INFO     | plugin.py | -------------- Response ----------------[🛬️]
2024-07-24 12:18:44 | INFO     | plugin.py | successful with status 200
2024-07-24 12:18:44 | DEBUG    | plugin.py | [type]: json      [time]: 1.226137
2024-07-24 12:18:44 | DEBUG    | plugin.py | [response]:
 {
  "cookies": {
    "sessioncookie": "123456789"
  }
}
.
2 passed in 5.36s
```
