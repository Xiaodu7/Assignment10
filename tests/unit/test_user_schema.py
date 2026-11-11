
import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError

from app.schemas.base import UserCreate
from app.schemas.user import UserRead


def test_user_read_excludes_password():
    """Check that passwords are not returned."""

    user_data = {
        "id": uuid4(),
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "is_active": True,
        "is_verified": False,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "password": "Secret123",
        "password_hash": "hashed_password"
    }

    user = UserRead.model_validate(user_data)
    result = user.model_dump()

    assert result["username"] == "testuser"
    assert "password" not in result
    assert "password_hash" not in result


def test_user_create_invalid_email():
    """Check that invalid email addresses are rejected."""

    with pytest.raises(ValidationError):
        UserCreate(
            first_name="Test",
            last_name="User",
            username="testuser",
            email="invalid-email",
            password="Secret123"
        )
