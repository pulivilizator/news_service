from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from core.enums import Language


class RegisterUser(BaseModel):
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_admin: bool = False

class User(RegisterUser):
    is_active: bool
    created_at: datetime
    updated_at: datetime