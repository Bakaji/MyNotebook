from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_name = models.CharField(unique=True, max_length=100)
    collection_description = models.CharField(max_length=1000, default='')
    collection_color = models.CharField(max_length=10, default='blue')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'created_at'


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=100, blank=False, null=False)
    note_content = models.CharField(max_length=100, default='')
    note_update_date = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)

    class Meta:
        order_with_respect_to = 'note_update_date'
        verbose_name_plural = 'notes'


class InvitationToken(models.Model):
    token = models.CharField(max_length=150, blank=False, null=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.user.username}'s token"
