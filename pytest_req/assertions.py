import json

from pytest_req.log import log
from pytest_req.utils.diff import AssertInfo, diff_json
from pytest_req.utils.jmespath import jmespath


class Expect:

    def __init__(self, response):
        self.response = response

    def to_be_ok(self) -> None:
        """
        assert status code == 200
        :return:
        """
        log.info(f"👀 assert Status code -> 200.")
        assert self.response.status_code == 200, f"Expected status code 200 but got {self.response.status_code}"

    def to_have_status_code(self, expected_status_code: int) -> None:
        """
        assert status code == expected status code
        :param expected_status_code:
        :return:
        """
        log.info(f"👀 assert Status code -> {expected_status_code}.")
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
        try:
            actual_json = self.response.json()
        except json.JSONDecodeError:
            raise AssertionError("Response does not contain valid JSON")

        AssertInfo.warning = []
        AssertInfo.error = []
        diff_json(actual_json, expected_json, exclude)
        if len(AssertInfo.warning) != 0:
            log.warning(AssertInfo.warning)
        if len(AssertInfo.error) != 0:
            assert "Response data" == "Assert data", (
                AssertInfo.error
            )

    def to_have_path_value(self, path, expected_value) -> None:
        """
        Assert path data
        doc: https://jmespath.org/
        :param path:
        :param expected_value:
        :return:
        """
        log.info(f"👀 assert path value -> {path} >> {expected_value}.")
        try:
            actual_json = self.response.json()
        except json.JSONDecodeError:
            raise AssertionError("Response does not contain valid JSON")

        search_value = jmespath(actual_json, path)
        assert search_value == expected_value, (
            f"expected value is different from the {expected_value}"
        )


def expect(response):
    return Expect(response)
