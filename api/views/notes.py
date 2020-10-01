from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import Note
from api.serializers.notes import NoteSerializer
from api.views.collections import find_collection
from note.responses import NotAuthenticatedResponse, NotFoundResponse, OKResponse, \
    BadRequestResponse, DeleteResponse


def find_note(note_id: int):
    try:
        return Note.objects.get(note_id=note_id)
    except:
        return None


def _check_request(request, collection_id):
    if not request.user.is_authenticated:
        return NotAuthenticatedResponse(), None
    if not (collection := find_collection(collection_id)):
        return NotFoundResponse('collection', collection_id), None
    return None, collection


class NotesListAPIView(APIView):
    @staticmethod
    def get(request, collection_id):
        if not request.user.is_authenticated:
            return NotAuthenticatedResponse()
        if not (collection := find_collection(collection_id)):
            return NotFoundResponse('collection', collection_id)
        data = Note.objects.filter(collection=collection)
        serial = NoteSerializer(data, many=True)
        return OKResponse(serial.data)


class NoteCreateAPIView(APIView):
    parser_classes = [JSONParser]

    @staticmethod
    def post(request: Request, collection_id):
        bad_response, collection = _check_request(request, collection_id)
        if bad_response:
            return bad_response
        request.data['collection'] = collection_id
        serial = NoteSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return OKResponse(serial.data)
        else:
            return BadRequestResponse(serial.errors)


class NoteUpdateAPIView(APIView):
    parser_classes = [JSONParser]

    @staticmethod
    def put(request: Request, collection_id, note_id):
        bad_response, collection = _check_request(request, collection_id)
        if bad_response:
            return bad_response
        if not (note := find_note(note_id)):
            return BadRequestResponse(['note not found'])
        if note.collection.collection_id != collection.collection_id:
            return BadRequestResponse(['note not in the collection'])
        serial = NoteSerializer(note, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return OKResponse(serial.data)
        else:
            return BadRequestResponse(serial.errors)


class NoteDeleteAPIView(APIView):
    @staticmethod
    def delete(request: Request, collection_id, note_id):
        bad_response, collection = _check_request(request, collection_id)
        if bad_response:
            return bad_response
        if not (note := find_note(note_id)):
            return BadRequestResponse(['note not found'])
        if note.collection.collection_id != collection.collection_id:
            return BadRequestResponse(['note not in the collection'])
        Note.delete(note)
        return DeleteResponse('note', note_id)


create_note = NoteCreateAPIView.as_view()
update_note = NoteUpdateAPIView.as_view()
delete_note = NoteDeleteAPIView.as_view()
get_all_notes = NotesListAPIView.as_view()
