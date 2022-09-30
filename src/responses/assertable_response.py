import allure
import jsonpath_rw
from requests import Response

from src.conditions.conditions import Condition
from src.custom_logging.configured_loguru_logger import loguru_logger


class AssertableResponse(object):
    def __init__(self, response: Response):
        self._response = response
        loguru_logger.info(
            f"REQUEST: \nmethod={response.request.method}, "
            f"\nurl={response.request.url}, "
            f"\nrequest_body={response.request.body}, "
            f"\nheaders={response.request.headers}"
        )
        loguru_logger.info(
            f"RESPONSE: \nstatus_code={response.status_code},"
            f" \nresponse_body={response.json()}, \nheaders={response.request.headers}"
        )

        allure.attach(
            f"REQUEST: url={response.request.url}, body={response.request.body}, headers={response.request.headers} "
            f"\nRESPONSE: status_code={response.status_code}, body={response.text} ",
            "log.txt",
            allure.attachment_type.TEXT,
        )

    @allure.step("Response should have {condition}")
    def should_have_condition(self, condition: Condition) -> None:
        condition.match(self._response)

    @allure.step(
        "Get field value from response by jsonpath [{json_path_to_field_in_response}]"
    )
    def get_field_value_from_response(self, json_path_to_field_in_response: str) -> str:
        parsed_field_value_from_response = ""
        try:
            response_json = self._response.json()
            parsed_field_value_from_response = (
                jsonpath_rw.parse(json_path_to_field_in_response)
                .find(response_json)[0]
                .value
            )
        except IndexError as index_error:
            loguru_logger.error(
                f"{repr(index_error)}."
                f" The response does not contain any field by jsonpath [{json_path_to_field_in_response}]"
            )
        return parsed_field_value_from_response

    def __repr__(self) -> str:
        return f"json response {self._response.json()}"
