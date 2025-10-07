from datetime import datetime
from pydantic import BaseModel

# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    id: int = 0
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []
    age: int = 0
    is_adult: bool = False

