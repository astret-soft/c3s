from typing import Optional

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.exceptions import DoesNotExist


class User(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    family_name = fields.CharField(max_length=50, null=True)
    name = fields.CharField(max_length=50, null=True)
    patronymic = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=30, default='misc')
    password_hash = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return password

    @classmethod
    async def create(cls, user: Optional[dict]) -> 'User':
        password_hash = cls.get_password_hash(user.password)
        model = cls(**user_dict, password_hash=password_hash)
        await model.save()
        return model

    def full_name(self) -> str:
        """
        Returns the full name
        """
        return ' '.join(filter(
            lambda x: x,
            (self.family_name, self.name, self.patronymic)
        )) or self.username

    class PydanticMeta:
        computed = ['full_name']
        exclude = ['password_hash']


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
