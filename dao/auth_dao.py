"""This unit contains a AuthDao class to interact with the database
for authentication purposes."""
from typing import Optional

from db.db_setup import db
from db.models import UserModel, UserSchema
# ----------------------------------------------------------------------


class UserDao:
    """
    This class implements the data access layer for authentication-related
    functionality.
    """
    def __init__(self) -> None:
        """
        Initialize the database session object.
        """
        self.session = db.session

    def add_new_user(self, user_data: UserSchema) -> Optional[UserModel]:
        """
        Add a new user to the database.

        Args:
            user_data (UserSchema): User data to be added to the database.

        Returns:
            UserModel: The newly created user object.
        """
        try:
            new_user = UserModel(**user_data.dict(exclude={'repeat_password'}))
            self.session.add(new_user)
            self.session.commit()
            self.session.close()

            return new_user
        except Exception as e:
            print(f"Failed to add user to the database, an exception is {e}")
            return None

    def get_user_by_email(self, email: str) -> Optional[UserModel]:
        """
        Retrieve a user from the database based on email address.

        Args:
            email (str): The email address of the user to be retrieved.

        Returns:
            UserModel: The user object that corresponds to the specified email
            address.
        """
        result = self.session.query(UserModel).filter(
            UserModel.email == email).first()

        return result
