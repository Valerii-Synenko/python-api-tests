import allure
from src.responses.assertable_response import AssertableResponse
from src.services.base_service import BaseApiService


class UserApiService(BaseApiService):
    def __init__(self):
        super().__init__()

    @allure.step("Register user")
    def register_user(self, user_body) -> AssertableResponse:
        return AssertableResponse(self._post("register", user_body))

    @allure.step("Delete user by id '{customer_id}'")
    def delete_user(self, customer_id: str) -> AssertableResponse:
        return AssertableResponse(self._delete(f"customers/{customer_id}"))
