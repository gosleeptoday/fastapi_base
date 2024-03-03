from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields, Tortoise

class Role(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255, null=False)
    permissions = fields.CharField(max_length=255, null=False)

class UserInfo(Model):
    id = fields.IntField(pk=True, index=True)
    FirstName = fields.CharField(max_length=255, null=False)
    SecondName = fields.CharField(max_length=255, null=False)
    SurName = fields.CharField(max_length=255, null=False)
    userid = fields.ForeignKeyField("models.User", related_name="user_id")

class User(Model):
    id = fields.IntField(pk=True, index=True)
    email = fields.CharField(max_length=255, null=False, unique=True)
    roleid = fields.ForeignKeyField("models.Role", related_name="role_id")
    password = fields.CharField(max_length=100, null=False, unique=True)

user_pydantic = pydantic_model_creator(User, name = "User", exclude= ["is_verified"])