from rest_framework import serializers

from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'note_id',
            'note_title',
            'note_content',
            'note_update_date',
            'collection'
        ]
