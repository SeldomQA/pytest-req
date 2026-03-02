import json
import requests

from pytest_req.log import log
from pytest_req.utils.diff import  AssertInfo, diff_json
from pytest_req.utils.jmespath import jmespath


class Expect:

    def __init__(self, response):
        self.response = response

    def to_be_ok(self) -> None:
        """
        assert status code == 200
        :return:
        """
        log.info(f"👀 assert status code -> 200.")
        assert self.response.status_code == 200, f"Expected status code 200 but got {self.response.status_code}"

    def to_have_status_code(self, expected_status_code: int) -> None:
        """
        assert status code == expected status code
        :param expected_status_code:
        :return:
        """
        log.info(f"👀 assert status code -> {expected_status_code}.")
        actual_status_code = self.response.status_code
        assert actual_status_code == expected_status_code, (
            f"Expected status code {expected_status_code} but got {actual_status_code}"
        )

    def to_have_json_matching(self, expected_json, exclude=None) -> None:
        """
        assert response JSON
        :param expected_json:
        :param exclude:
        :return:
        """
        log.info(f"👀 assert JSON -> {expected_json}.")
        actual_json = self.response
        if isinstance(self.response, requests.Response):
            try:
                actual_json = self.response.json()
            except json.JSONDecodeError:
                raise AssertionError("Response does not contain valid JSON")

        AssertInfo.clear()
        diff_json(actual_json, expected_json, exclude)
        if AssertInfo.warning:
            for warn in AssertInfo.warning:
                log.warning(warn)
        if AssertInfo.error:
            raise AssertionError(f"JSON mismatch:\n {AssertInfo.error}")


    def to_have_path_value(self, path, expected_value) -> None:
        """
        Assert path data
        doc: https://jmespath.org/
        :param path:
        :param expected_value:
        :return:
        """
        log.info(f"👀 assert path value -> {path} >> {expected_value}.")
        actual_json = self.response
        if isinstance(self.response, requests.Response):
            try:
                actual_json = self.response.json()
            except json.JSONDecodeError:
                raise AssertionError("Response does not contain valid JSON")

        search_value = jmespath(actual_json, path)
        assert search_value == expected_value, (
            f"expected value is different from the {expected_value}"
        )

    def to_have_path_contains(self, path, expected_value) -> None:
        """
        Assert path data contains expected value
        doc: https://jmespath.org/
        :param path:
        :param expected_value:
        :return:
        """
        log.info(f"👀 assert path contains -> {path} >> {expected_value}.")
        actual_json = self.response
        if isinstance(self.response, requests.Response):
            try:
                actual_json = self.response.json()
            except json.JSONDecodeError:
                raise AssertionError("Response does not contain valid JSON")

        search_value = jmespath(actual_json, path)
        if isinstance(search_value, (str, list, dict)):
            assert expected_value in search_value, (
                f"expected value '{expected_value}' is not found in '{search_value}'"
            )
        else:
            raise AssertionError(f"The value at path '{path}' is not a containable type (str/list/dict)")

    def to_have_path_all_equal(self, path, expected_value) -> None:
        """
        Assert all values in list at path equal expected_value
        """
        log.info(f"👀 assert path all equal -> {path} == {expected_value}.")
        actual_json = self.response
        if isinstance(self.response, requests.Response):
            try:
                actual_json = self.response.json()
            except json.JSONDecodeError:
                raise AssertionError("Response does not contain valid JSON")

        search_value = jmespath(actual_json, path)

        if not isinstance(search_value, list):
            raise AssertionError(f"The value at path '{path}' is not a list")

        if not search_value:
            log.info("ℹ️ list is empty, skip all-equal assertion")
            return

        for index, value in enumerate(search_value):
            assert value == expected_value, (
                f"Index {index}: expected {expected_value}, but got {value}"
            )

    def to_have_path_all_contains(self, path, expected_value) -> None:
        """
        Assert all values in list at path contain expected_value
        """
        log.info(f"👀 assert path all contains -> {path} contains {expected_value}.")
        actual_json = self.response
        if isinstance(self.response, requests.Response):
            try:
                actual_json = self.response.json()
            except json.JSONDecodeError:
                raise AssertionError("Response does not contain valid JSON")

        search_value = jmespath(actual_json, path)

        if not isinstance(search_value, list):
            raise AssertionError(f"The value at path '{path}' is not a list, it is {type(search_value)}")

        if not search_value:
            log.info("ℹ️ list is empty, skip all-contains assertion")
            return

        for index, item in enumerate(search_value):
            assert expected_value in str(item), (
                f"Index {index}: expected to contain '{expected_value}', but got '{item}'"
            )

def expect(response):
    return Expect(response)
