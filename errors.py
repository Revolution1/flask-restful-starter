# encoding=utf-8

from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    def __init__(self, data):
        self.code = 400
        self.data = data
        HTTPException.__init__(self)


class NotFound(HTTPException):
    def __init__(self, data):
        self.code = 404
        self.data = data
        HTTPException.__init__(self)
