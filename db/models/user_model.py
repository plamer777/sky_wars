"""This unit contains models and schemas to work with the user's data"""
import re
from typing import Optional

from db.db_setup import db
from pydantic import BaseModel, EmailStr, ValidationError, root_validator
# ----------------------------------------------------------------------


class UserModel(db.Model):
    """UserModel class is a model representing a user"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), default='customer')
    first_name = db.Column(db.String(30), default=None)
    last_name = db.Column(db.String(30), default=None)


class UserSchema(BaseModel):
    """UserSchema class serves as serializer and deserializer"""
    email: EmailStr
    password: str | bytes
    repeat_password: str | bytes
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: str = 'customer'

    @root_validator
    def validate_password(cls, values: dict) -> dict:
        """Password validation method"""
        regex = r"\A[a-zA-Z0-9]{8,20}\Z"
        compiler = re.compile(regex)
        password = values.get('password')
        repeat_password = values.get('repeat_password')

        if password != repeat_password:
            raise ValidationError('The entered passwords do not match')

        elif not compiler.match(password):
            raise ValidationError('Password has incorrect format')

        return values

    class Config:
        orm_mode = True


class UserAuthSchema(BaseModel):
    """This schema serves to validate existing user"""
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
