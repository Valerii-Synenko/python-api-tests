import abc

import jsonpath_rw
from hamcrest import assert_that
from hamcrest.core.matcher import Matcher
from requests import Response


class Condition(object):
    @abc.abstractmethod
    def match(self, response: Response):
        return


class StatusCodeCondition(Condition):
    def match(self, response: Response) -> None:
        assert_that(response.status_code, self._hamcrest_matcher)

    def __init__(self, hamcrest_matcher: Matcher):
        super().__init__()
        self._hamcrest_matcher = hamcrest_matcher

    def __repr__(self):
        return f"status code {self._hamcrest_matcher}"


status_code = StatusCodeCondition


class BodyFieldCondition(Condition):
    def match(self, response: Response) -> None:
        try:
            parsed_field_value_from_response = (
                jsonpath_rw.parse(self._json_path_to_field_in_response)
                .find(response.json())[0]
                .value
            )
            assert_that(parsed_field_value_from_response, self._hamcrest_matcher)
        except IndexError as index_error:
            assert_reason = (
                f"{repr(index_error)}."
                f" The response does not contain any field by jsonpath: "
                f"'{parsed_field_value_from_response}'"
            )
            assert_that(False, reason=assert_reason)

    def __init__(self, json_path: str, hamcrest_matcher: Matcher):
        super().__init__()
        self._json_path_to_field_in_response = json_path
        self._hamcrest_matcher = hamcrest_matcher

    def __repr__(self):
        return (
            f"body field [{self._json_path_to_field_in_response}] = "
            f"{self._hamcrest_matcher}"
        )


body_field = BodyFieldCondition
