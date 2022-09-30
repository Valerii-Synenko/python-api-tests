from hamcrest import equal_to, not_none

from src.conditions.conditions import status_code, body_field
from src.responses.assertable_response import AssertableResponse


def test_can_register_new_user_with_valid_credentials(models, faker, api_services):
    user_model = models.user_model(
        username=faker.name(), password=faker.password(), email=faker.email()
    )

    response: AssertableResponse = api_services.user_api_service().register_user(
        user_model
    )

    response.should_have_condition(status_code(equal_to(200)))
    response.should_have_condition(body_field("$.id", not_none()))


def test_can_delete_existing_user(models, faker, api_services):
    user_model = models.user_model(
        username=faker.name(), password=faker.password(), email=faker.email()
    )

    user_id: str = (
        api_services.user_api_service()
        .register_user(user_model)
        .get_field_value_from_response("$.id")
    )

    response: AssertableResponse = api_services.user_api_service().delete_user(user_id)

    response.should_have_condition(status_code(equal_to(200)))
