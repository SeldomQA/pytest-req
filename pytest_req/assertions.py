class Expect:

    def __init__(self, response):
        self.response = response

    def to_be_ok(self):
        assert self.response.status_code == 200, f"Expected status code 200 but got {self.response.status_code}"

    def to_have_status_code(self, expected_status_code):
        actual_status_code = self.response.status_code
        assert actual_status_code == expected_status_code, (
            f"Expected status code {expected_status_code} but got {actual_status_code}"
        )


def expect(response):
    return Expect(response)
