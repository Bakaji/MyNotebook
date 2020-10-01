from rest_framework import serializers

from api.models import Collection, Note


class CollectionGeneralInfo(serializers.ModelSerializer):
    notes_count = serializers.SerializerMethodField()

    @staticmethod
    def get_notes_count(obj):
        return Note.objects.filter(collection=obj).count()

    class Meta:
        model = Collection
        fields = ('collection_id',
                  'collection_name',
                  'collection_description',
                  'created_at',
                  'collection_color',
                  'notes_count',)
