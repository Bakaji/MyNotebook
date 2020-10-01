from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api.views.auth.register import request_token, register_user
from api.views.collections import update_collection, list_collections, create_collection, \
    delete_collection, get_collection
from api.views.notes import get_all_notes, create_note, update_note, delete_note

urlpatterns = (
    path('auth/login/', obtain_auth_token),
    path('auth/request_token/', request_token),
    path('auth/register/', register_user),

    path('collections/', list_collections),
    path('collections/create/', create_collection),

    path('collections/<int:collection_id>/', get_collection),
    path('collections/<int:collection_id>/update/', update_collection),
    path('collections/<int:collection_id>/delete/', delete_collection),

    path('collections/<int:collection_id>/notes/', get_all_notes),
    path('collections/<int:collection_id>/notes/create/', create_note),
    path('collections/<int:collection_id>/notes/<int:note_id>/update/', update_note),
    path('collections/<int:collection_id>/notes/<int:note_id>/delete/', delete_note),
)
