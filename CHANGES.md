## 0.7.0

* 增加断言方法 `to_match_schema()`。

## 0.6.0

* 增加断言方法 `to_have_path_all_contains()`。

## 0.5.3

* 功能：兼容非`base_url`域名的请求。

## 0.5.2

* 增加：`to_have_path_all_equal()` 断言方法, 断言列表的所有值是否相等。
* 增强：接口调用日志增加 IP 地址的显示。

## 0.5.1

* 修复：使用`base_url`, 日志不显示完整的URL地址的问题。
* 增强：`expect()` 断言方法不仅支持传Repsone对象，还支持`dict`、`list` 等。

## 0.5.0

* 增加断言方法 `to_have_path_contains()`。

## 0.4.0

* 增加`req()` 方法。


## 0.3.0

* 增加`expect`断言类
    * `expect(response).to_be_ok()`
    * `expect(response).to_have_status_code()`
    * `expect(response).to_have_json_matching()`
    * `expect(response).to_have_path_value()`

## 0.2.0

* 增加`head`、`options` 等fixture。
* session增加`patch`、`head`、`options`方法。

## 0.1.0

* 完成`pytest-req`插件。
    * 支持`get/post/put/delete/patch/session`等fixture。
    * 支持日志显示接口请求和影响信息。
    * 支持base-url。