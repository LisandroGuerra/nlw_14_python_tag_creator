class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = 'Unprocessable Entity'
        self.status_code = 422
        
