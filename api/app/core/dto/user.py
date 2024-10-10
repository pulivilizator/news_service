from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class UserRegister(BaseModel):
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_admin: bool = False

class User(UserRegister):
    is_active: bool
    created_at: datetime
    updated_at: datetime
