from django.db import models
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import uuid
from django.http import JsonResponse


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    # is_admin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'user'
        verbose_name = 'user'


class TagsModel(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    tag_name  = models.CharField('tag_name',max_length=255,unique=True)
    scope  = models.CharField('scope',max_length=255,blank=True)
    user_id = models.ForeignKey(UserProfile, to_field='user_id', null=True, blank=True, on_delete=models.SET_NULL, db_column='user_id')

    # def to_json(self):
    #     json_representation = {
    #         'tag_id': self.tag_id,
    #         'tag_name': self.tag_name,
    #         'scope': self.scope,
    #         'user_id': self.user_id
    #     }
    #     return json_representation

    class Meta:
        managed = True
        db_table = 'tags'
        verbose_name = 'tags'


class VM(models.Model):
    vm_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    vm_name = models.CharField('vm_name', max_length=255, unique=True)
    creation_date = models.DateTimeField('creation_date', auto_now_add=True)
    tags = models.ManyToManyField('TagsModel', related_name='vms')

    class Meta:
        managed = True
        db_table = 'vms'
        verbose_name = 'vms'

