# encoding=utf-8

from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES


class HTTPError(HTTPException):
    def __init__(self, description=None, response=None, code=None):

        super(HTTPError, self).__init__(description=description, response=response)
        self.response = response
        self.description = description
        self.code = code or self.status_code

    def __str__(self):
        err_type = ''
        message = HTTP_STATUS_CODES.get(self.code, 'Unknown Error')
        if self.is_client_error():
            err_type = 'Client Error: '
        elif self.is_server_error():
            err_type = 'Server Error: '
        if self.description:
            message = '{} {} {}("{}")'.format(self.status_code, err_type, message, self.description)
        return message

    __repr__ = __str__

    @property
    def status_code(self):
        if self.code:
            return self.code
        if self.response is not None:
            return self.response.status_code

    def is_client_error(self):
        if self.status_code is None:
            return False
        return 400 <= self.status_code < 500

    def is_server_error(self):
        if self.status_code is None:
            return False
        return 500 <= self.status_code < 600

class APIException(HTTPError):
    def __init__(self, data):
        self.code = 400
        self.data = data
        HTTPException.__init__(self)


class NotFound(HTTPError):
    def __init__(self, data):
        self.code = 404
        self.data = data
        HTTPException.__init__(self)
