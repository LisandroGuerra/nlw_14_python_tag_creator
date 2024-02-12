from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # Send the error message to a log
        # Send the error message to an external service
        # Send the error message to a monitoring service
        # Sende an email to the development team
        # etc
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.error_type,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
