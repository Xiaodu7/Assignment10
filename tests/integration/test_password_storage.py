
from sqlalchemy import select
from app.models.user import User


def test_password_stored_as_hash(db_session):
    """Verify that passwords are stored securely."""

    plain_password = "MySecure123"

    user_data = {
        "first_name": "Test",
        "last_name": "Student",
        "username": "storage_test",
        "email": "storage_test@example.com",
        "password": plain_password
    }

    # Register and save the user
    user = User.register(db_session, user_data)
    db_session.commit()

    # Read the password hash from the database
    stored_hash = db_session.execute(
        select(User.password_hash).where(
            User.id == user.id
        )
    ).scalar_one()

    # Make sure the password is not stored as plain text
    assert stored_hash != plain_password

    # Verify the password
    assert user.verify_password(plain_password) is True
    assert user.verify_password("WrongPassword123") is False
