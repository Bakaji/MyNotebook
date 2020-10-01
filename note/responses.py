from rest_framework import status
from rest_framework.response import Response

_MESSAGE = 'message'


class NotAuthenticatedResponse(Response):
    def __init__(self):
        super(NotAuthenticatedResponse, self).__init__(data={_MESSAGE: "User not authenticated"},
                                                       status=status.HTTP_401_UNAUTHORIZED)


class NotAuthorisedResponse(Response):
    def __init__(self):
        super(NotAuthorisedResponse, self).__init__(
            data={_MESSAGE: "User not authorised for this action"},
            status=status.HTTP_403_FORBIDDEN)


class NotFoundResponse(Response):
    def __init__(self, entity_name: str, object_name: str):
        super(NotFoundResponse, self).__init__(data={_MESSAGE: f'{entity_name} : {object_name} '
                                                               f'not found'},
                                               status=status.HTTP_404_NOT_FOUND)


class OKResponse(Response):
    def __init__(self, data):
        super(OKResponse, self).__init__(data=data)
        self.status_code = status.HTTP_200_OK


class DeleteResponse(OKResponse):
    def __init__(self, entity, identifier):
        data = {'message': f'{entity} {str(identifier)} deleted'}
        super(DeleteResponse, self).__init__(data=data)


class BadRequestResponse(Response):
    def __init__(self, data):
        super(BadRequestResponse, self).__init__(data=data, status=status.HTTP_400_BAD_REQUEST)
