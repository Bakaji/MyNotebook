from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import Collection
from api.serializers.collections import CollectionGeneralInfo
from note.responses import NotAuthenticatedResponse, OKResponse, BadRequestResponse, \
    NotFoundResponse, DeleteResponse


class CollectionListAPIView(APIView):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            serial = CollectionGeneralInfo(Collection.objects.all(), many=True)
            return OKResponse(serial.data)
        else:
            return NotAuthenticatedResponse()


class CollectionGetAPIView(APIView):
    @staticmethod
    def get(request, collection_id):
        if not request.user.is_authenticated:
            return NotAuthenticatedResponse()
        if not (collection := find_collection(collection_id)):
            return NotFoundResponse("collection", collection_id.__str__())
        serial = CollectionGeneralInfo(collection)
        return OKResponse(serial.data)


def find_collection(coll_id: int):
    try:
        return Collection.objects.get(collection_id=coll_id)
    except:
        return None


class CollectionCreateAPIView(APIView):
    parser_classes = [JSONParser]

    @staticmethod
    def post(request: Request):
        if not request.user.is_authenticated:
            return NotAuthenticatedResponse()
        serial = CollectionGeneralInfo(data=request.data)
        if serial.is_valid():
            serial.save()
            return OKResponse(serial.data)
        else:
            return BadRequestResponse(serial.errors)


class CollectionUpdateAPIView(APIView):
    parser_classes = [JSONParser]

    @staticmethod
    def put(request, collection_id: int):
        if not request.user.is_authenticated:
            return NotAuthenticatedResponse()
        if not (collection := find_collection(collection_id)):
            return NotFoundResponse("collection", collection_id.__str__())
        serial = CollectionGeneralInfo(collection, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return OKResponse(serial.data)
        else:
            return BadRequestResponse(serial.errors)


class CollectionDeleteAPIView(APIView):

    @staticmethod
    def delete(request, collection_id):
        if not request.user.is_authenticated:
            return NotAuthenticatedResponse()
        if not (collection := find_collection(collection_id)):
            return NotFoundResponse("collection", collection_id.__str__())
        Collection.delete(collection)
        return DeleteResponse('collection', collection_id)


list_collections = CollectionListAPIView.as_view()
get_collection = CollectionGetAPIView.as_view()
update_collection = CollectionUpdateAPIView.as_view()
create_collection = CollectionCreateAPIView.as_view()
delete_collection = CollectionDeleteAPIView.as_view()
