# pytest-req

```shell
                 __            __                             
    ____  __  __/ /____  _____/ /_            ________  ____ _
   / __ \/ / / / __/ _ \/ ___/ __/  ______   / ___/ _ \/ __ `/
  / /_/ / /_/ / /_/  __(__  ) /_   /_____/  / /  /  __/ /_/ / 
 / .___/\__, /\__/\___/____/\__/           /_/   \___/\__, /  
/_/    /____/                                           /_/   

```

> pytest requests plugin

pytest 使用 requests 库的插件。

## 特点

* 完全兼容Requests库的使用。
* 提供详细的`请求/响应`日志，并支持可配置。
* 轻量级，非侵入。

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
# test_req.py

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
# test_session.py

def test_session(session):
    """
    test session, keep requests cookie
    """
    s = session
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    s.get('https://httpbin.org/cookies')
```

__⭐ 支持base-url__

```python
# test_base_url.py

def test_req_base_url(get):
    """
    test base url
    pytest --base-url=https://httpbin.org
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

- `-s` 查看详细日志。
- `--base-url` 设置接口基础URL，用例当中进需要配置路径。

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
