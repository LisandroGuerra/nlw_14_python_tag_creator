from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    This class is responsible for creating a tag
    responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest):
        '''
        This method is responsible for validating and creating a tag
        '''

        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body.get('product_code')

        formatted_response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
