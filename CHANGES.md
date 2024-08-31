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