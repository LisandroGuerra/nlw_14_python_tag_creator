# pylint: disable=redefined-outer-name
import pytest
from src.views.tag_creator_view import TagCreatorView
from src.views.http_types.http_request import HttpRequest

CODE = '123-456-789'

@pytest.fixture
def http_request():
    return HttpRequest(body={'product_code': CODE})

expected_response = {
        "data": {
            "type": "Tag Image",
            "count": 1,
            "path": f"{CODE}.png"
        }
    }


def test_validate_and_create_success(http_request):
    view = TagCreatorView()
    response = view.validate_and_create(http_request)

    assert response.status_code == 200
    assert response.body == expected_response
