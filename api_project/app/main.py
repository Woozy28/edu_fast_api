# main.py
import uvicorn
from fastapi import FastAPI
import logger
import config
import models

app = FastAPI()

user = models.User(name="John Doe", id=1)
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
    3: {"username": "alice_jones", "email": "alice@example.com"},
    4: {"username": "bob_white", "email": "bob@example.com"},
}

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, 
           {"username": "katya", "user_info": "любит петь"}]

feedback_db = [
    {"username":'user','feedback':'feedback'}

]
# Гет к корневому каталогу.
@app.get("/")  
def read_root():
    return {"message": "Hello, World!"}

# simply random chapter
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

#get users with limits, name and email parameters 
@app.get("/all_users/")
def read_users(username: str = None, email: str = None, limit: int = 10):
    filtered_users = fake_users

    if username:
        filtered_users = {key: user for key, user in filtered_users.items() if username.lower() in user["username"].lower()}

    if email:
        filtered_users = {key: user for key, user in filtered_users.items() if email.lower() in user["email"].lower()}

    return dict(list(filtered_users.items())[:limit])


@app.get("/userss", response_model= models.User)
def read_user_info():
    return user

#pot new user with calculation his adult 
@app.post("/user")
def new_user(user: models.User):
    if user.age >=18:
        user.is_adult = True
    return user

@app.post("/feedback")
def new_feedback(feedback: models.Feedback):
    feedback_db.append([{'username':feedback.username, 'feedback':feedback.feedback}]) 
    return {"message": f"Feedback received. Thank you, {feedback.username}."}

#get user by id
@app.get('/users_by_id/{user_id}') # тут объявили параметр пути
async def get_users_by_id(user_id: int): # тут указали его тип данных
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

#delete user by id
@app.delete('/delete_users/{user_id}')
async def delete_user(user_id: int):
    return {"message": f"Пользователь с ID {user_id} был удален"}


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}                  

@app.get('/users')
async def get_all_users():
    return fake_db

# Конечная точка для добавления нового пользователя
@app.post('/add_user' , response_model=models.User)
async def add_user(user: models.User):  # Используем модель для валидации данных
    fake_db.append({"useown beyond rname": user.username, "user_info": user.user_info})
    return {"message": "Юзер успешно добавлен в базу данных"}

@app.post('/create_user' , response_model=models.UserCreate)
async def create_user(user: models.UserCreate):  # Используем модель для валидации данных
    
    return user


from config import load_config

config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False


# запускаем сервак увикорн 
if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)    