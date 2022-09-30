from _pytest.fixtures import fixture
from faker import Faker
from src.models.models_factory import Models
from src.services.services_factory import ApiServices


@fixture
def faker():
    return Faker()


@fixture
def models():
    return Models()


@fixture
def api_services():
    return ApiServices()
