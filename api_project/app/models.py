from datetime import datetime
from pydantic import BaseModel, Field, field_validator

# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    id: int = 0
    signup_ts: datetime | None = None
    friends: list[int] = []
    username: str = "John Doe"
    age: int = 0
    is_adult: bool = False
    user_info: str = 'None'

class Feedback(BaseModel):
    username: str = "User"
    feedback: str = Field(max_length=500, min_length=10)
    @field_validator('feedback')
    def validate_message(cls, feedback):
        # Недопустимые слова
        bad_words = ["редиска", "бяка", "козявка"]

        if any(word in feedback for word in bad_words):
            raise ValueError(f'Использование недопустимых слов.')

        return feedback    

class UserCreate(BaseModel):  
    name: str = 'name',
    email: str = "email",
    age: int = 0,
    is_subscribed: bool = False
