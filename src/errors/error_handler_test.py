# pylint: disable=redefined-outer-name
import pytest
from src.errors.error_handler import handle_errors
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

@pytest.fixture
def generic_exception():
    return Exception('Generic error')

@pytest.fixture
def unprocessable_entity_error():
    return HttpUnprocessableEntityError('Unprocessable entity error')


def test_error_handler_status_code_500(generic_exception):
    response = handle_errors(generic_exception)
    assert response.status_code == 500
    assert response.body == {
            "errors": [{
                "title": "Internal Server Error",
                "detail": "Generic error"
            }]
        }

def test_error_handler_status_code_422(unprocessable_entity_error):
    response = handle_errors(unprocessable_entity_error)
    assert response.status_code == 422
    assert response.body == {
            "errors": [{
                "title": "Unprocessable Entity",
                "detail": "Unprocessable entity error"
            }]
        }
